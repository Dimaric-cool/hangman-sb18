from turtle import *

WIDTH = 800
HEIGHT = 700

Screen().setup(WIDTH, HEIGHT)


shape("turtle")
speed(3)
shapesize(1.5)

pensize(10)
penup()
dlinaSlova = 7
dlinakwadr = 70
otstup = 40
X = - (dlinaSlova * dlinakwadr + (dlinaSlova - 1) * otstup) // 2
Y = 0

for x in range(dlinaSlova):
    goto(X, Y)
    pendown()
    for _ in range(4):
        forward(dlinakwadr)
        right(90)
    penup()
    X += dlinakwadr + otstup


mainloop()