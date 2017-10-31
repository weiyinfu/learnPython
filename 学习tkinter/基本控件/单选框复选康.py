import tkinter

root = tkinter.Tk()

r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root, variable=r, value='1', text='Radio1')
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='2', text='Radio2')
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='3', text='Radio3')
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='4', text='Radio4')
radio.pack()

c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root, text='CheckButton', variable=c, onvalue=1, offvalue=2)
check.pack()

v = tkinter.StringVar()
v.set('check python')


def clk():
    v.set("clk")


# 绑定v到Checkbutton的属性textvariable
tkinter.Checkbutton(root, text='check python', textvariable=v, command=clk).pack()
vv = tkinter.IntVar(value=1)
tkinter.Checkbutton(root, variable=vv, text='checkbutton value', command=lambda: vv.set(0 if vv.get()else 3)).pack()
vvv = tkinter.StringVar()


def callCheckbutton():
    print(vvv.get())


tkinter.Checkbutton(root,
                    variable=v,
                    text='checkbutton value',
                    onvalue='python',  # 设置On的值
                    offvalue='tkinter',  # 设置Off的值
                    command=callCheckbutton).pack()
root.mainloop()
print(r.get())
print(c.get())
