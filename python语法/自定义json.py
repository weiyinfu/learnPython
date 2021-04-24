import json
from typing import Any

"""
自定义JSON序列化有两种方式，实际上，只需要重写default函数就足够了，完全不需要使用cls参数指定JSONEncoder。
JSONEncoder对JSON序列化的方式控制粒度更大，可以通过此类来重新定义数组、int等对象的序列化方式，而使用default参数则只有在默认JSONEncoder不行的时候才会调用default函数。
"""


class Haha:
    def __init__(self):
        self.name = "haha"


def default(o: Any) -> Any:
    if type(o) == Haha:
        return {'name': o.name}
    raise Exception("unhandled")


class CommonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return default(o)


try:
    print(json.dumps([Haha()]))
except:
    print('果然不行')
    pass
print(json.dumps([Haha()], cls=CommonEncoder))
print(json.dumps([Haha()], default=default))
