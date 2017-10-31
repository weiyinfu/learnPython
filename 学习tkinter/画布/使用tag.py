# 使用属性tags设置item的tag
# 使用Canvas的方法gettags获取指定item的tags
from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 使用tags指定一个tag('r1')
rt = cv.create_rectangle(10, 10, 110, 110, tags='r1')
cv.pack()
print(cv.gettags(rt))
# 使用tags属性指定多个tags,即重新设置tags的属性
cv.itemconfig(rt, tags=('r2', 'r3', 'r4'))
print(cv.gettags(rt))
root.mainloop()
