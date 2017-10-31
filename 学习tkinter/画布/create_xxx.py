import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=600, height=480, bg='white')
#img = tkinter.PhotoImage(file = 'smile.gif')
#canvas.create_image(300, 50, image=img)
canvas.create_text(300, 75, text='Use Canvas', fill='blue')
canvas.create_text(302, 77, text='Use Canvas', fill='gray')
canvas.create_polygon(290, 114, 316, 114, 330, 130, 310, 146, 284, 146, 270, 130)
canvas.create_oval(280, 120, 320, 140, fill='white')
canvas.create_line(250, 130, 350, 130)
canvas.create_line(300, 100, 300, 160)
canvas.create_rectangle(90, 190, 510, 410, width=5)
canvas.create_arc(100, 200, 500, 400, start=0, extent=240, fill='pink')
canvas.create_arc(103, 203, 500, 400, start=241, extent=118, fill='red')
canvas.pack()

root.mainloop()