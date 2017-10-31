import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='haha', db='test')
cur = connection.cursor(pymysql.cursors.DictCursor)
cur.execute("select * from employee where name=%s", "weidiao")
print(cur.fetchall())
# 占位符始终是%s
cur.execute("insert into employee values(%s,%s)", ("haha", 234))
cur.execute("select*from employee")
print(cur.fetchall())
