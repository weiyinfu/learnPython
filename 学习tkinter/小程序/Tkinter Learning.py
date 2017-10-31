from tkinter import *
window=Tk()
l=Label(text='weidiao')
l.pack()
g=Canvas(width=100,height=100)
g.create_oval(10,10,90,90,fill='green')
g.pack()
window.update()
window.mainloop()
