#原理是将json中的每一个属性值都变成了Obj类型
foo = {'a': 1,
       'b': 2,
       'c': {'a': 22
             }
       }


class Obj(object):
    def __getattribute__(self, name):
        if isinstance(object.__getattribute__(self, name), dict):
            setattr(self, name, type(name, (type(self),),
                                     object.__getattribute__(self, name))())
        return object.__getattribute__(self, name)

Foo = type('Foo', (Obj,), foo)()
print(type(Foo))
print(Foo.c.a)
