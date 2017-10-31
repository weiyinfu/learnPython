"""
Add decorator for each method of a class.
"""
import functools
import threading


class DecorateClass(object):
    def decorate(self):
        for name, fn in self.iter():
            if callable(fn):
                self.operate(name, fn)  # 在派生类中必须包含operate方法


class LockerDecorator(DecorateClass):
    def __init__(self, obj, lock=threading.RLock()):
        self.obj = obj
        self.lock = lock

    def iter(self):
        return [(name, getattr(self.obj, name)) \
                for name in dir(self.obj) if not name.startswith('_')]

    def operate(self, name, fn):
        @functools.wraps(fn)
        def locker(*args, **kv):
            self.lock.acquire()
            try:
                return fn(*args, **kv)
            finally:
                self.lock.release()

        setattr(self.obj, name, locker)


class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    def acquire(self):
        print("mylocker.acquire() called.")

    def release(self):
        print("mylocker.unlock() called.")


class Foo(object):
    def __init__(self):
        # Enable one or more decorators for each method:
        LockerDecorator(self).decorate()
        LockerDecorator(self, mylocker()).decorate()

    def interface1(self):
        print(" interface1() called.")

    def interface2(self):
        print(" interface2() called.")

    def _interface3(self):
        print("_interface3() called.")


if __name__ == "__main__":
    obj = Foo()
    obj.interface1()
    obj.interface2()
    obj.interface1()
    obj.interface2()
    obj._interface3()
    print(obj.interface1.__name__)
    '''
    print(dir(obj))
    print("---------------------")
    for item in [(name,getattr(obj, name)) for name in dir(obj)]:
        print(item)'''
