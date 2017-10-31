## 一、使用pymysql
使用pymysql替代MysqlDb，将下面这句话放在wsgi.py、manage.py文件中

```
import pymysql
pymysql.install_as_MySQLdb()
```

## 二、数据库迁移命令
```
检测models文件有哪些变化
python manage.py makemigrations

进行更新操作
python manage.py migrate

```


在settings最后加上日志，使得打印SQL语句，
这样就可以在控制台下观察何时触发SQL查询了。

## 三、使用日志打印SQL语句
```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
```
