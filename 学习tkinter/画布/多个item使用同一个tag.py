from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 使用tags指定一个tag('r1')
rt = cv.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))
cv.pack()
rt2 = cv.create_rectangle(20, 20, 80, 80, tags='r3')
print(cv.find_withtag('r3'))
for item in cv.find_withtag('r3'):
    cv.itemconfig(item, outline='blue')
root.mainloop()
