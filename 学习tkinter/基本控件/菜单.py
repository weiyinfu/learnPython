import tkinter

root = tkinter.Tk()

menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Open')
submenu.add_command(label='Save')
submenu.add_command(label='Close')
menu.add_cascade(label='File', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Copy')
submenu.add_command(label='Paste')
submenu.add_separator()
submenu.add_command(label='Cut')
menu.add_cascade(label='Edit', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='About')
menu.add_cascade(label='Help', menu=submenu)

root.config(menu=menu)
root.mainloop()