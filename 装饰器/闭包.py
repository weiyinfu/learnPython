from threading import Timer
import time

timer_interval = 1


def f():
    for i in range(10):
        def go():
            print(i)

        t = Timer(timer_interval, go)
        t.start()


f()
while True:
    time.sleep(0.1)
    print('main running')
