from tkinter import *
root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.pack(side = RIGHT,fill = Y)
#解除Listbox的yscrollcommand与Scrollbar的set绑定
#lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert(END,str(i))
#使用索引为50的元素可见
lb.see(50)
lb.pack(side = LEFT)
sl['command'] = lb.yview
root.mainloop()