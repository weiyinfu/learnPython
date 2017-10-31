def bar():
    print("bar")


def inject(cls):
    cls.bar = bar
    print(cls.__name__)
    return cls


@inject
class Foo(object):
    pass


foo = Foo()
foo.bar()
