import multiprocessing as mp
import threading
import time


def eventloop():
    while 1:
        time.sleep(3)
        print("i am son")


def startup():
    x = threading.Thread(target=eventloop)
    x.start()


mp.Process(target=startup).start()

while 1:
    time.sleep(2)
    print("i am parent")
