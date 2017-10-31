from tkinter import *


class Window:
    def __init__(self, master):
        self.master = master
        master.title("tkinter sandbox")
        master.geometry("800x450")
        master.resizable(0, 0)
        master.config(background='black')

        master.columnconfigure(0, pad=3)
        master.columnconfigure(1, pad=3)
        master.columnconfigure(2, pad=3)

        master.rowconfigure(0, pad=3)
        master.rowconfigure(1, pad=3)
        master.rowconfigure(2, pad=3)

        self.canvas = Canvas(master, width=400, height=200)
        self.canvas.grid(row=1, column=2, sticky=E)

        self.label = Label(master, text="Enter Color:", background='black', fg='white')
        self.label.grid(row=0, column=0, sticky=W)

        self.text_input = Entry(master, bd='0')
        self.text_input.grid(row=0, column=1, sticky=W)

        self.print_text = Button(master, text="Change Background Color", command=self.change_color,
                                 highlightbackground='black')
        self.print_text.grid(row=0, column=2, sticky=W)

        self.x1_i = Entry(master, bd='0')
        self.text_input.grid(row=1, column=0, padx=3, sticky=W)

        self.y1_i = Entry(master, bd='0')
        self.text_input.grid(row=1, column=0, padx=3, sticky=W)

        self.draw_line_button = Button(master, text="Draw Line",
                                       command=self.draw_line(self.x1_i, self.y1_i, 20, 30, 4),
                                       highlightbackground='black')
        self.draw_line_button.grid(row=1, column=0, padx=3, sticky=W)

        self.close_button = Button(master, text="Close", command=master.quit, highlightbackground='black')
        self.close_button.grid(row=2, column=2, sticky=S + W)

    def change_color(self):
        self.input_color = self.text_input.get()
        self.master.config(background=self.input_color)
        self.label.config(background=self.input_color)
        self.text_input.config(bd='0')
        self.print_text.config(highlightbackground=self.input_color)
        self.draw_line_button.config(highlightbackground=self.input_color)
        self.close_button.config(highlightbackground=self.input_color)
        if (self.input_color == 'black'):
            self.label.config(fg='white')
        else:
            self.label.config(fg='black')

    def draw_line(self, line_x1, line_y1, line_x2, line_y2, line_width):
        self.x1 = line_x1
        self.y1 = line_y1
        self.x2 = line_x2
        self.y2 = line_y2
        self.width = line_width
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=self.width)


root = Tk()
Window_var = Window(root)
root.mainloop()
