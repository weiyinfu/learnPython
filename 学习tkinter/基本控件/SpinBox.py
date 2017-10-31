from tkinter import *

root = Tk()


def printSpin():
    # 使用get()方法来得到当前的显示值
    sb.insert(END, '.00')
    print
    sb.get()


sb = Spinbox(root,
             from_=1234,  # 最小值
             to=9999,  # 最大值
             increment=1,
             command=printSpin  # 回调函数
             )
sb.pack()
v = StringVar()
sb = Spinbox(root,
             values=(0, 2, 20, 40, -1),
             increment=2,
             textvariable=v
             )
v.set(200)
sb.pack()
print(v.get())
root.mainloop()
