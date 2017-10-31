import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='haha', db='test', charset='utf8')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute(
    """select * from Employee where name={weidiao} and name={weidiao}"""
        .format(**{"weidiao": "'weidiao'"}))
print(effect_row)
data = cursor.fetchall()
print(data)
print(cursor.description)
print(type(cursor.description))
print(type(data[0]))
# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])


# 提交，不然无法保存新建或者修改的数据
conn.commit()
cursor.close()

conn.close()
