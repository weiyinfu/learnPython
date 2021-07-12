import time

import schedule

x = schedule.Scheduler()

"""
实践证明：schedule这个库运行每个任务的时候并非是异步的。

schedule是一个阻塞式、单线程的库。

它的语法就是every，每次执行完一个任务的时候，它会计算任务下次应该什么时间执行。
"""


def task1():
    print(time.time(), "task1", one.next_run)
    time.sleep(10)  # schedule这个库是根据next_run()来执行的，如果一个任务迟迟没有执行完，那么这个任务的next_run就始终没有更新，就导致当前任务频繁运行


def task2():
    print(time.time(), "task2", two.next_run)


one = x.every(3).seconds.do(task1)
two = x.every(7).seconds.do(task2)

while 1:
    time.sleep(1)
    x.run_pending()
