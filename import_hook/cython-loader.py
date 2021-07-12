import sys
import types
from typing import List

from setuptools import setup

from bes.util import form

"""
don't change the order of the import 
"""
import importlib
import multiprocessing as mp
import os
from importlib.abc import PathEntryFinder, Loader
from importlib.machinery import ModuleSpec
from distutils.extension import Extension
from os.path import *
from bes.log import logger
import glob2
import numpy as np
from Cython.Build import cythonize

from tqdm.auto import tqdm

"""
单独的pyx文件编译工具
"""
import tempfile


def compile_file(filepath: str, so_name: str = None):
    """
    编译一个pyx文件
    :param filepath:pyx文件的地址
    :param so_name: so文件的名称，也就是编译之后的包名
    :return:
    """
    if not filepath.endswith('.pyx'):
        raise Exception(f"{filepath} is not pyx file")
    if not exists(filepath):
        raise Exception(f"{filepath} not exist")
    old_dir = os.path.abspath(os.curdir)
    os.chdir(os.path.dirname(filepath))
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    if not so_name:
        so_name = name
    setup(
        ext_modules=cythonize(
            [
                Extension(
                    so_name,
                    [filename],
                    include_dirs=[np.get_include()],
                    extra_compile_args=["-w"],
                    extra_link_args=["-w"],
                    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]
                )
            ],
            build_dir=tempfile.mkdtemp(),  # 把一些中间代码生成到这个临时文件夹中
            compiler_directives={'language_level': "3"},  # 编译级别O3
        ),
        script_name=__file__,
        script_args=['build_ext', '-i']
    )
    os.chdir(old_dir)


def get_pyx_so_name(pyx_path: str) -> str:
    """
    根据pyx文件的内容获取目标模块的名称，目的是保持一个文件内容对应一个so文件，只要pyx文件没有改，so文件就不需要改
    :param pyx_path:
    :return:
    """
    if not exists(pyx_path):
        raise Exception(f"{pyx_path} not exists")
    content = open(pyx_path).read()
    content_hash = form.md5(content)
    new_so_name = f"haha{content_hash}"
    return new_so_name


def should_compile(pyx_path: str, so_path: str = None):
    # 根据文件的新老判断是否应该编译，用于lazy进行编译
    folder, (name, _) = dirname(pyx_path), splitext(basename(pyx_path))
    if so_path is None:
        so_path = f"{folder}/{name}.*.so"
        so_file_candidates = glob2.glob(so_path)
        if len(so_file_candidates) == 1:
            so_path = so_file_candidates[0]
    if so_path and exists(so_path):
        if os.stat(so_path).st_mtime > os.stat(pyx_path).st_mtime:
            # so文件更改时间更靠后，则不执行编译过程
            logger.info(f"文件没有发生变化，跳过编译{pyx_path}")
            return False
    return True


def compile_folder(folder: str, lazy: bool = True):
    # 编译一个文件夹下的全部pyx文件
    folder = os.path.abspath(folder)
    res = join(folder, '**', "*.pyx")
    ps: List[mp.Process] = []
    for filepath in tqdm(glob2.glob(res), desc='compiling cython'):
        if lazy and not should_compile(filepath):
            continue
        p = mp.Process(target=compile_file, args=(filepath, None))
        p.start()
        ps.append(p)
    for i in ps:
        i.join()


def import_pyx(pyx_path: str, pkg: str):
    """
    通过mock 模块的方式导入pyx文件
    :param pyx_path:
    :param pkg:
    :return:
    """
    if not exists(pyx_path):
        raise Exception(f"{pyx_path} not exists")
    so_name = get_pyx_so_name(pyx_path)
    so_path = join(dirname(pyx_path), so_name)
    if not exists(so_path):
        compile_file(pyx_path, so_name)
    so_list = glob2.glob(join(os.path.dirname(pyx_path), so_name + "*.so"))
    if not so_list:
        raise Exception(f"找不到编译完的so文件")
    if len(so_list) > 1:
        raise Exception(f"so文件有点多呀")
    new_so_path = so_list[0]
    mod_path = f"{pkg}.{so_name}"
    ans = importlib.import_module(mod_path)
    os.remove(new_so_path)  # 加载完成之后就可以删除这个so包了
    return ans


def reload_so_module(mod: types.ModuleType):
    # 重新加载一个cython模块
    so_path = os.path.abspath(mod.__file__)
    so_file_name = basename(so_path)
    name = so_file_name[:so_file_name.index('.')]
    folder = dirname(so_path)
    pyx_path = join(folder, name + '.pyx')
    ans = import_pyx(pyx_path, mod.__package__)
    copy_module(mod, ans)


def copy_module(src: types.ModuleType, des: types.ModuleType):
    keep_attr = '__file__ __name__ __package__ __loader__ __path__ __spec__'.split()
    for i in set(dir(des)) - set(dir(src)):
        delattr(des, i)
    for i in dir(src):
        if i in keep_attr:
            continue
        setattr(des, i, getattr(src, i))


class CythonLoader(Loader):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.lock = mp.Lock()
        self.m = mp.Manager()
        self.modules = self.m.dict()

    def load_module(self, fullname: str):
        if fullname in self.modules:
            return self.modules[fullname]
        with self.lock:
            if fullname in self.modules:
                return self.modules[fullname]
            logger.info(f'loading pyx module {fullname}')
            res = types.ModuleType(fullname)
            mod = import_pyx(self.filepath, '.'.join(fullname.split(".")[:-1]))
            copy_module(mod, res)
            sys.modules[fullname] = res
            self.modules[fullname] = res
            return res


class CythonImporter(PathEntryFinder, Loader):
    """
    import的时候需要考虑并发，每次只有一个进程进入此实例
    """
    path_prefix: List[str] = []

    @classmethod
    def find_spec(cls, fullname: str, path: List[str], target):
        # demo:fullname=bes.alg path=['/Users/bytedance/Desktop/mypy3/bes_data/bes'] target=None,path表示父包所在的目录
        if path is None or len(path) == 0:
            return
        if type(path) != list:
            return
        if type(path[0]) != str:
            return
        yes = False
        for i in cls.path_prefix:
            if fullname.startswith(i):
                yes = True
                break
        if not yes:
            return
        # logger.info(f'find_spec  {fullname}, {path}, {target}')
        pyx_path = os.path.join(path[0], fullname.split(".")[-1] + ".pyx")
        if not exists(pyx_path):
            return
        loader = CythonLoader(pyx_path)
        ans = ModuleSpec(name=fullname, loader=loader)
        return ans


inited = False


def use_hook(path_prefix: List[str]):
    """
    使用cython import hook，inited确保只初始化一次
    :return:
    """
    global inited
    if inited:
        return
    inited = True
    CythonImporter.path_prefix = path_prefix
    sys.meta_path.insert(0, CythonImporter)
