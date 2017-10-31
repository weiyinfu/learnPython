import inspect


def f(x, y):
    z = inspect.getargvalues(inspect.currentframe())
    print(z, type(z))
    return x + y


f(3, 4)

print('=' * 20, 'use decorator', '=' * 20)


def decorator1(arg1):
    def mydeco(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            finally:
                print
                arg1

        return wrapper

    return mydeco


@decorator1("bb")
def show3(x):
    print(x)


@decorator1("bb")
def show4(x, y):
    print(x)
    print(y)


show3("hello , world !")
show4("hello ", " world !")
