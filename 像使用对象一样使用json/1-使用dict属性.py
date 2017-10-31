class DottableDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

    def allowDotting(self, state=True):
        if state:
            self.__dict__ = self
        else:
            self.__dict__ = dict()


d = DottableDict()
d.allowDotting()
d.foo = 'bar'
print(d['foo'])
# bar
print(d.foo)
# bar
d.allowDotting(state=False)
print(d['foo'])
# bar from http://www.jb51.net
print(d.foo)
# AttributeError: 'DottableDict' object has no attribute 'foo'
