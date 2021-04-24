from queue import SimpleQueue

"""
队列
"""
x = SimpleQueue()
x.put(1)
x.put(2)
print(x.get())

from queue import LifoQueue

"""
栈
"""
x = LifoQueue()
x.put(1)
x.put(2)
print(x.get())
from queue import Queue  # 这个也是一个队列

x = Queue()
x.put(1)
x.put(2)
print(x.get())


