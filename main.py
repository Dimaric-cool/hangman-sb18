from turtle import *

WIDTH = 800
HEIGHT = 700

Screen().setup(WIDTH, HEIGHT)


shape("turtle")
speed(3)
shapesize(1.5)

pensize(10)
penup()

dlinaSlova = 3

X = -250
Y = -200

for x in range(dlinaSlova):
    goto(X, Y)
    pendown()
    for _ in range(4):
        forward(50)
        right(90)
    penup()
    X += 50 + 20


mainloop()