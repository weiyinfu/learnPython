from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
d = {1: PIESLICE, 2: CHORD, 3: ARC}
for i in d:
    cv.create_arc(
        (10, 10 + 60 * i, 110, 110 + 60 * i),
        style=d[i],  # 指定样式
        start=30,  # 指定起始角度
        extent=30  # 指定角度偏移量
    )
cv.pack()
root.mainloop()
# 使用三种样式，分别创建了扇形、弓形和弧形
