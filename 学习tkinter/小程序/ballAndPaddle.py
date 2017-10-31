import random
from tkinter import *


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # x,y为小球运动方向矢量
        self.x = random.choice([-3, -2, -1, 1, 2, 3])
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 350, 200, 360, fill=color)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if self.x:
            if self.x + pos[0] < 0: self.x = -pos[0]
            if self.x + pos[2] > self.canvas.winfo_width(): self.x = self.canvas.winfo_width() - pos[2]
            self.canvas.move(self.id, self.x, 0)
            self.x = 0

    def turn_left(self, event):
        self.x = -5

    def turn_right(self, event):
        self.x = 5


tk = Tk()
tk.title("weidiao's game")
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


def mainloop():
    if ball.hit_bottom:
        tk.quit()
    ball.draw()
    paddle.draw()
    tk.update()
    tk.after(10, mainloop)


mainloop()
tk.mainloop()
print('you died!')
