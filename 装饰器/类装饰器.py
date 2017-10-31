class Foo(object):
    def __init__(self, func):
        super(Foo, self).__init__()
        self._func = func

    def __call__(self):
        print('class decorator')
        self._func()


@Foo
def bar():
    print("bar")


bar()
