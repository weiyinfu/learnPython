from tkinter import *
import time
import random
from math import *

window = Tk()
# window.wm_attributes('-topmost',1)
g = Canvas(window, width=1000, height=700)
g.pack()
window.update()
window.title('A crowd catches One--made by weidiao.neu')

reminder = g.create_text(g.winfo_width() / 2, g.winfo_height() / 2, text='Press up,down,left,right arrow to move',
                         fill='purple', font=('Concolas', 30))
window.update()
time.sleep(3)
g.delete(reminder)

speed = 5
AC = 30
faster = 3
me = g.create_oval(10, 10, 40, 40, fill='red')
hunter = []


def left(e):
   p = g.coords(me)
   if p[0] - speed * faster < 0: return
   g.move(me, -speed * faster, 0)


def right(e):
   p = g.coords(me)
   if p[2] + speed * faster > g.winfo_width(): return
   g.move(me, speed * faster, 0)


def up(e):
   p = g.coords(me)
   if p[1] - speed * faster < 0: return
   g.move(me, 0, -speed * faster)


def down(e):
   p = g.coords(me)
   if p[3] + speed * faster > g.winfo_height(): return
   g.move(me, 0, speed * faster)


g.bind_all('<KeyPress-Left>', left)
g.bind_all('<KeyPress-Right>', right)
g.bind_all('<KeyPress-Down>', down)
g.bind_all('<KeyPress-Up>', up)


def newHunter():
   print("newhunter")
   x = random.randrange(0, g.winfo_width())
   y = random.randrange(0, g.winfo_height())
   p = g.coords(me)
   if hypot(x - p[0], y - p[1]) < AC * 7:
      return
   hunter.append(g.create_oval(x - AC, y - AC, x + AC, y + AC, fill='green'))
   for i in range(0, len(hunter) - 1):
      if collapse(hunter[i], hunter[len(hunter) - 1], 0, 0):
         g.delete(hunter[len(hunter) - 1])
         del hunter[len(hunter) - 1]
         return


def collapse(i, j, dx, dy):
   pi = g.coords(i)
   pj = g.coords(j)
   xi = (pi[0] + pi[2]) / 2.0 + dx
   yi = (pi[1] + pi[3]) / 2.0 + dy
   xj = (pj[0] + pj[2]) / 2.0
   yj = (pj[1] + pj[3]) / 2.0
   if hypot(xi - xj, yi - yj) < AC * 2:
      return True
   else:
      return False


def canGo(i, dx, dy):
   for j in range(0, len(hunter)):
      if i == j: continue
      if collapse(hunter[i], hunter[j], dx, dy): return False
   return True


start = time.time()
caught = False


def mainloop():
   global  caught
   if caught: window.quit()
   window.after(200,mainloop)
   if random.randint(0, 50) ==0:
      newHunter()
   pos = g.coords(me)

   for i in range(0, len(hunter)):
      t = g.coords(hunter[i])
      if hypot(t[0] + t[2] - pos[0] - pos[2], t[1] + t[3] - pos[3] - pos[1]) < AC:
         caught = True

      dx = pos[0] + pos[2] - t[0] - t[2]
      dy = pos[1] + pos[3] - t[1] - t[3]
      the = atan2(dx, dy)
      l = hypot(dx, dy)
      dx = speed * dx / l
      dy = speed * dy / l

      if canGo(i, dx, dy):
         g.move(hunter[i], dx, dy)
      else:
         the = random.randint(0, 1000) / 1000.0
         dx = speed * cos(the)
         dy = speed * sin(the)
         if canGo(i, dx, dy):
            g.move(hunter[i], dx, dy)

mainloop()
window.mainloop()

g.create_text(g.winfo_width() / 2, g.winfo_height() / 2, text='you continued:%s seconds' % (time.time() - start),
              fill='purple', font=('Concolas', 30))
window.update()
#window.after(10000,window.quit)
window.mainloop()
