import os
import signal
import sys
import time

import fastapi
import uvicorn

from bes.log import logger

app = fastapi.FastAPI()


def term(sig_num, addtion):
    logger.info("term is called")
    # sys.exit(0)# sys.exit不管用
    os.killpg(os.getp(os.getpid()), signal.SIGKILL)


def init_signal():
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)


def background_task():
    while 1:
        time.sleep(3)
        print("hello")


@app.on_event("startup")
async def startup_event():
    """
    注意服务启动的时候做的事情必须是deamon，否则可能导致进程无法退出
    :return:
    """
    init_signal()  # 加上这句话就能够让进程成功退出
    import threading
    th = threading.Thread(target=background_task)
    th.daemon = False
    th.start()


@app.on_event("shutdown")
async def shutdown_event():
    """
    注意服务启动的时候做的事情必须是deamon，否则可能导致进程无法退出
    :return:
    """
    sys.exit(0)


uvicorn.run(app)
