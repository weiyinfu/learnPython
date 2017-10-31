############画刷填充###
from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
cv.create_rectangle(10, 10, 110, 110,
                    outline='red',
                    stipple='gray12',
                    fill='green')
cv.pack()
root.mainloop()
