import json
import os
import sys
import types
from importlib.abc import PathEntryFinder, Loader
from importlib.machinery import ModuleSpec

cur_dir = os.path.dirname(__file__)


class JsonLoader(Loader):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_module(self, fullname):
        print('load_module', fullname)
        res = types.ModuleType(fullname)
        content = json.load(open(self.filepath))
        res.__dict__.update(content)
        sys.modules[fullname] = res
        return res

class JsonImporter(PathEntryFinder, Loader):
    @classmethod
    def find_spec(cls, fullname, path, target):
        print('find_spec', fullname, path, target)
        filepath = None
        for i in (f"{fullname}.json", os.path.join(cur_dir, f"{fullname}.json")):
            if os.path.exists(i):
                filepath = i
                break
        if filepath is None:
            return
        loader = JsonLoader(filepath)
        ans = ModuleSpec(name=fullname, loader=loader)
        return ans


sys.meta_path.insert(0, JsonImporter)
import baga
import baga
import importlib
print("reload-----")
importlib.reload(baga)
print("reload===")
print(type(sys), type(baga))
print(dir(baga))
print(baga.a)
print(baga.b)
# 此处reload的类型不是module，故报错
# from importlib import reload
# reload(baga)
