import tkinter
from tkinter import messagebox

def cmd():
    global n
    global buttontext
    n += 1
    if n==1:
        messagebox.askokcancel('Python Tkinter', 'askokcancel')
        buttontext.set('askquestion')
    elif n==2:
        messagebox.askquestion('Python Tkinter', 'askquestion')
        buttontext.set('askyesno')
    elif n==3:
        messagebox.askyesno('Python Tkinter', 'askyesno')
        buttontext.set('showerror')
    elif n==4:
        messagebox.showerror('Python Tkinter', 'showerror')
        buttontext.set('showinfo')
    elif n==5:
        messagebox.showinfo('Python Tkinter', 'showinfo')
        buttontext.set('showwarning')
    else:
        n = 0
        messagebox.showwarning('Python Tkinter', 'showwarning')
        buttontext.set('askokcancel')

n = 0
root = tkinter.Tk()
buttontext = tkinter.StringVar()
buttontext.set('askokcancel')
button = tkinter.Button(root, textvariable=buttontext, command=cmd)
button.pack()
root.mainloop()