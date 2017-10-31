from tkinter import *
root = Tk()
cv = Canvas(root,bg = 'white')
# 创建两个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
# 将y坐标放大为原来的2位，x坐标值不变
cv.scale(rt1,0,0,1,2)
cv.pack()
root.mainloop()
# scale的参数为(self,xoffset,yoffset,xscale,yscale)