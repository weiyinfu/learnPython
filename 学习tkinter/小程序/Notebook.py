import tkinter.ttk as ttk
import tkinter

parent = tkinter.Tk()
n = ttk.Notebook(parent)
f1 = ttk.Frame(n)  # 小程序 page, which would get widgets gridded into it
f2 = ttk.Frame(n)  # second page
label1=tkinter.Label(f1,text="label1")
label2=tkinter.Label(f2,text="hhaa")
label1.pack()
label2.pack()
n.add(f1, text='One')
n.add(f2, text='Two')
n.pack()
n.update()
parent.mainloop()
