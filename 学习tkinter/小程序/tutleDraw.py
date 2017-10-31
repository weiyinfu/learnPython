import turtle
import random

t = turtle.Pen()


def circle(x, y, r):
    t.up()
    t.goto(x, y)
    t.color(random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0)
    t.down()
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def rectangle(x, y, w, h):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0)
    t.begin_fill()
    t.setheading(0)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.end_fill()


def star(x, y, n, l):
    t.up()
    t.setheading(0)
    t.goto(x, y)
    t.down()
    t.color(random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0, random.randint(0, 1000) / 1000.0)
    av = (n - 2) * 180.0 / n
    little = 180 - av * 2
    t.begin_fill()
    for i in range(0, n * 2):
        t.forward(l)
        if i % 2 == 1:
            t.left(180 - av)
        else:
            t.left(180 - little)
    t.end_fill()


def randomDraw():
    for i in range(1, 20):
        if random.randint(0, 3) == 0:
            x = random.randint(0, 300)
            y = random.randint(0, 300)
            r = random.randint(100, 200)
            circle(x, y, r)
        elif random.randint(0, 2) == 0:
            x = random.randint(0, 300)
            y = random.randint(0, 300)
            w = random.randint(0, 300)
            h = random.randint(0, 300)
            rectangle(x, y, w, h)
        else:
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            n = random.randint(3, 10)
            l = random.randint(30, 100)
            star(x, y, n, l)


randomDraw()
