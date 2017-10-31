"""
dec，dec2是装饰器，分别修饰f和f2
dec没有使用functools.wraps，所以丢失函数元信息
"""


def dec(f):
    def ff():
        f()

    return ff


def dec2(f):
    import functools
    @functools.wraps(f)
    def ff():
        f()

    return ff


@dec
def f():
    """I am the doc string of f()"""
    print(f.__name__, f.__module__, f.__doc__)


@dec2
def f2():
    """I am the doc string of f2()"""
    pass


print(f.__name__, f.__doc__)
print(f2.__name__, f2.__doc__)
