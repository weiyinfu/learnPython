import logging
from logging import LogRecord

logging.root.setLevel(logging.INFO)
handler = logging.StreamHandler()
form = '%(asctime)s pid=%(process)d logid=%(_logid)s %(filename)s:%(lineno)s %(funcName)s [%(name)s]-%(levelname)s: %(message)s'
handler.setFormatter(logging.Formatter(form))


class MyFilter(logging.Filter):
    def filter(self, record: LogRecord) -> int:
        print(dir(record))
        print(getattr(record,'lineno'))
        record._logid='haha'
        return 0


handler.addFilter(MyFilter())
logging.root.addHandler(handler)
logging.info('good morning')
