import multiprocessing as mp


def go():
    from 脚本任务.testMultiProcessImport import lib


a = [mp.Process(target=go) for _ in range(10)]
for i in a:
    i.start()

