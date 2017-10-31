from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 创建三个rectangle
rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags=('r1', 'r2', 'r3'))


def printRect(event):
    print('rectangle')


# 绑定item与事件
cv.tag_bind('r1', '<Button-1>', printRect)
cv.pack()
root.mainloop()
