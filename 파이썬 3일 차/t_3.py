import turtle as t

angle = 360/8
color = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']

t.color('red')
t.pensize(5)

for i in range(48):
    t.forward(100)
    t.left(angle)

t.right(120)

for i in range(6):
    t.forward(100)
    t.left(angle)

for i in range(4):

    t.forward(100)
    t.right(60)
    for i in range(6):
        t.forward(100)
        t.left(angle)


t.done()