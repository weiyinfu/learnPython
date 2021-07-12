import multiprocessing as mp
import threading
import time

l = threading.Lock()

"""
线程锁只能用于控制同一个进程内的并发。
进程锁既能够用于控制同一个进程内的并发，同时也能够用于控制多个进程内的并发。
"""


def go(name):
    with l:
        while 1:
            time.sleep(1)
            print(name)


a = [mp.Process(target=go, args=(f"{i}",)) for i in range(3)]
for i in a:
    i.daemon = True
    i.start()
time.sleep(100)
