class Person:
    def __init__(self):
        pass

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__
        else:
            raise Exception('no this attribute', item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


p = Person()
p.age = 3
p.name = 'weidiao'
print(p.age, p.__dict__)
