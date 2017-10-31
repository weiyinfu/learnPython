from tkinter import *

root = Tk()
x = Scale(root,
          from_=0,  # 设置最大值
          to=100.0,  # 设置最小值
          orient=HORIZONTAL,  # 设置水平方向
          label='choice:',  # 设置标签值
          )
x.pack()
print(x.get())
root.mainloop()
