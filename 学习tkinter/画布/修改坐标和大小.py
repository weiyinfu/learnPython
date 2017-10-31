from Tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
rt = cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    stipple = 'gray12',
                    fill = 'green')
cv.pack()
# 重新设置rt的坐标（相当于移动一个item）
cv.coords(rt,(40,40,80,80))
root.mainloop()
# 动态修改item的坐标