import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='haha', db='test', charset='utf8')
cur=connection.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute("select * from employee")
print(cur.fetchall())
cur=connection.cursor()
cur.execute("select * from employee")
print(cur.fetchall())
cur.close()
connection.close()