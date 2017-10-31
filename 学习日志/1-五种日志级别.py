import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
"""
4个主要的组件
logger: 日志类，应用程序往往通过调用它提供的api来记录日志；
handler: 对日志信息处理，可以将日志发送(保存)到不同的目标域中；
filter: 对日志信息进行过滤；
formatter:日志的格式化；

5个级别
"""