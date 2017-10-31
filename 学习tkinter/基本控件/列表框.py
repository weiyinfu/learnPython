from tkinter import *

root = Tk()

lb0 = Listbox(root, selectmode=BROWSE)
for item in ['python', 'tkinter', 'widget']:
    lb0.insert(END, item)
lb0.pack()

lb1 = Listbox(root, selectmode=BROWSE)
for item in ['python', 'tkinter', 'widget']:
    lb1.insert(END, item)
lb1.pack()

lb2 = Listbox(root, selectmode=MULTIPLE)
for item in ['python', 'tkinter', 'widget']:
    lb2.insert(END, item)
lb2.delete(0, 3)
lb2.insert(0, *"weidiao is great".split())
lb2.selection_set(0, 2)
print(lb2.size())
print(lb2.curselection())
lb2.pack()
root.mainloop()
