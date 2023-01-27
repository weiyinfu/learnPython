import CppHeaderParser as cp
import os
from os.path import *
from pprint import pprint
import pycparser as pc

p = "/Users/bytedance/Desktop/pico/PlatformSdkLoader/PlatformSdkCommon/include"


def one():
    for i in os.listdir(p):
        filepath = join(p, i)
        cppHeader = cp.CppHeader(filepath)
        for f in cppHeader.functions:
            pprint(f)
            input()
            # print(f['name'])


def two():
    # 这个库会报错
    x = pc.parse_file('/Users/bytedance/Desktop/pico/PlatformSdkLoader/app/src/main/cpp/Register.cpp', True)
    print(type(x), dir(x))
    input()


two()
# one()
