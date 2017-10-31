import tkinter
from tkinter import *

root = tkinter.Tk()
Button(root, anchor=tkinter.E, text='Button1', width=40, height=5).pack()
Button(root, text='Button2', bg='blue').pack()
Button(root, text='Button3', width=14, height=1).pack()
Button(root, text='Button4', width=60, height=5, state=tkinter.DISABLED).pack()
# relief属性
Button(root, text='hello button', relief=FLAT).pack()
Button(root, text='hello button', relief=GROOVE).pack()
Button(root, text='hello button', relief=RAISED).pack()
Button(root, text='hello button', relief=RIDGE).pack()
Button(root, text='hello button', relief=SOLID).pack()
Button(root, text='hello button', relief=SUNKEN).pack()
root.mainloop()
