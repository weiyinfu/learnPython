import multiprocessing as mp
import threading
import time

l = mp.Lock()
"""
答案是可以：锁是有粒度的。
* 协程锁
* 线程锁
* 进程锁
"""

def go(name):
    with l:
        while 1:
            time.sleep(1)
            print(name)


a = [threading.Thread(target=go, args=(f"{i}")) for i in range(3)]
for i in a:
    i.daemon = True
    i.start()
time.sleep(100)
