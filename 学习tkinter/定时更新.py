import time
from tkinter import *


def tick():
   t = time.strftime('%H:%M:%S')
   clock.config(text=t)
   clock.after(200, tick)


root = Tk()
status = Label(root, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=0, column=0)
clock = Label(root, font=('Consolas', 20, 'bold'), bg='green')
clock.grid(row=0, column=1)
tick()
root.mainloop()
