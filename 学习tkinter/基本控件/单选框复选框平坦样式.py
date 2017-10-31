import tkinter

root = tkinter.Tk()

r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root, variable=r, value='1', text='Radio1', indicatoron=0)
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='2', text='Radio2', indicatoron=0)
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='3', text='Radio3', indicatoron=0)
radio.pack()

radio = tkinter.Radiobutton(root, variable=r, value='4', text='Radio4', indicatoron=0)
radio.pack()

c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root, text='CheckButton', variable=c, onvalue=1, offvalue=2, indicatoron=0)
check.pack()

root.mainloop()
print(r.get())
print(c.get())