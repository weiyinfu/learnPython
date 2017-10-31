# 使用addtag_来向上一个或下一个item添加tag
from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3'))
rt2 = cv.create_rectangle(
    20, 20, 80, 80,
    tags=('s1', 's2', 's3'))
rt3 = cv.create_rectangle(
    30, 30, 70, 70,
    tags=('y1', 'y2', 'y3'))
# 向rt2的上一个item添加r4
cv.addtag_above('r4', rt2)
# 向rt2的下一个item添加r5
cv.addtag_below('r5', rt2)

for item in [rt1, rt2, rt3]:
    print
    cv.gettags(item)

cv.pack()
root.mainloop()
# Canvas使用了stack的技术，新创建的item总是位于前一个创建的item之上，故调用above时，它会查找rt2上面的item为rt3,故rt3中添加了tag('r4')，同样add_below会查找下面的item。
