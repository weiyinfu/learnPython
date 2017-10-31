import tkinter

from  PIL import Image, ImageTk


def setImage(canvas):
    img = ImageTk.PhotoImage(Image.open("../beauty/0.jpg"))
    x = canvas.create_image(300, 300, image=img)
    return img


window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400, bg='green')
img = setImage(canvas)
canvas.pack()
window.mainloop()
