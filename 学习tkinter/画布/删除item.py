from tkinter import *

root = Tk()
cv = Canvas(root, bg='white')
# 创建两个rectangle
rt1 = cv.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3'))
r2 = cv.create_rectangle(
    20, 20, 110, 110,
    tags=('s1', 's2', 's3'))
# 使用id删除rt1
cv.delete(rt1)
# 使用tag删除r2
cv.delete('s1')

cv.pack()
root.mainloop()