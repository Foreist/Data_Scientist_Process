import turtle as t
import math as m


t.color('blue')
t.pensize(5)
t.forward(200)
t.left(90)
t.forward(200)
t.left(135)
t.forward(m.sqrt(200 ** 2 + 200 ** 2))
t.right(135)
t.forward(200)
t.right(135)
t.forward(m.sqrt(200 ** 2 + 200 ** 2))
t.left(135)
t.forward(200)
t.left(90)
t.forward(200)
t.right(135)
t.forward((m.sqrt(200 ** 2 + 200 ** 2)) /2)
t.right(90)
t.forward((m.sqrt(200 ** 2 + 200 ** 2)) /2)
t.done()