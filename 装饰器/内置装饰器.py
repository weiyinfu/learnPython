"""
内置装饰器指built_in装饰器，有三个
* staticmethod
* classmethod
* property
"""


class Foo:
    def __init__(self, var):
        self._var = var

    @property
    def var(self):
        return self._var

    @var.getter
    def var(self):
        print("var.getter")
        return self._var

    # 如果不定义var.setter，给var赋值就会出错
    @var.setter
    def var(self, var):
        self._var = var
        print("var.setter")


foo = Foo('var 1')
print(foo.var)
foo.var = 'var 2'
print(foo.var)
