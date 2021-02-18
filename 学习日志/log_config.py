import logging.config

good_format = '%(asctime)s %(haha)s process=%(process)d %(filename)s:%(lineno)s %(funcName)s [%(name)s]-%(levelname)s: %(message)s'


class LogIdFileter(logging.Filter):
    def filter(self, record):
        record.haha = 'haha'  # 此处设置新值，可以再good_format中添加此值
        # 此处return True表示通过过滤，可以打印
        return True


logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': good_format
        },
    },
    'filters': {
        'logid_filter': {
            '()': LogIdFileter,
        }
    },
    'handlers': {
        'log_agent': {
            'level': 'INFO',
            'class': 'bytedlogger.StreamLogHandler',
            'tags': {},
            'formatter': 'default',
            'filters': ['logid_filter'],
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['logid_filter'],
        },
    },
    'root': {
        'handlers': ['log_agent', 'console'],
        'level': "INFO",
    },
}
logging.config.dictConfig(logging_config)
logging.info("hello world")
