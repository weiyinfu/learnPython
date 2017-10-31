import logging

handler = logging.StreamHandler()
handler.addFilter(logging.Filter('a.b.c'))
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.WARNING)
logger1 = logging.getLogger('a.b.c.d')
logger2 = logging.getLogger('x.y')
logger1.addHandler(handler)
logger2.addHandler(handler)
logger2.error("hello")
logger1.error("hello")
logging.error("why")
