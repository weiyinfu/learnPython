from math import *
from time import *
from tkinter import Tk
from turtle import Canvas

window = Tk()
g = Canvas(width=300, height=300)
g.pack()
centerX = 150.0
centerY = 150.0
r = 130.0


def drawFrame():
   frame = g.create_oval(centerX - r, centerY - r, centerX + r, centerY + r, width=2)
   the = 2 * pi / 60.0
   for i in range(0, 60):
      now = the * i
      len = 5.0;
      width = 2.0
      if i % 5 == 0: len = 15.0;width = 5.0
      g.create_line(centerX + (r - len) * cos(now - pi / 2), centerY + (r - len) * sin(now - pi / 2),
                    centerX + r * cos(now - pi / 2), centerY + r * sin(now - pi / 2), width=width)


drawFrame()
ti = 0.0
nothing = -1
dt = 1.0


class Pointer:
   def __init__(self, r, width, color, period):
      self.r = r
      self.width = width
      self.color = color
      self.period = period
      self.id = nothing

   def update(self):
      g.delete(self.id)
      now = (ti % self.period) / self.period * 2 * pi
      self.id = g.create_line(centerX, centerY, centerX + self.r * cos(now - pi / 2),
                              centerY + self.r * sin(now - pi / 2), fill=self.color, width=self.width)


hour = Pointer(r * 0.5, 7, 'red', 12 * 3600.0)
minute = Pointer(r * 0.7, 4, 'yellow', 3600.0)
second = Pointer(r * 0.9, 2, 'blue', 60.0)


def update():
   global ti
   ti = ti + dt
   if ti == 12 * 3600: ti = 0
   hour.update()
   second.update()
   minute.update()
   sleep(1)
   window.update()
   window.after(1000,update)

update()
window.mainloop()
