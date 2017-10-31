from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10, 10, 110, 110,
    width=8,
    tags=('r1', 'r2', 'r3'))


def printRect(event):
    print('rectangle')


def printLine(event):
    print('line')


# 绑定item与左键事件
cv.tag_bind('r1', '<Button-1>', printRect)
# 绑定item与右键事件
cv.tag_bind('r1', '<Button-3>', printLine)
# 创建一个line，并将其tags设置为'r1'
cv.create_line(10, 200, 100, 200, width=5, tags='r1')
cv.pack()
root.mainloop()
