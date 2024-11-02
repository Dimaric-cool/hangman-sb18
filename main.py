from turtle import *

WIDTH = 800
HEIGHT = 700

Screen().setup(WIDTH, HEIGHT)


shape("turtle")
speed(3)
shapesize(1.5)

pensize(10)
penup()
dlinaSlova = 4
dlinakwadr = 50
otstup = 20
X = - (dlinaSlova * dlinakwadr + (dlinaSlova - 1) * otstup) // 2
Y = -250

for x in range(dlinaSlova):
    goto(X, Y)
    pendown()
    for _ in range(4):
        forward(dlinakwadr)
        right(90)
    penup()
    X += dlinakwadr + otstup

# линия 1
penup()
goto(-350,-175)
pendown()
goto(-30,-175)
penup()

# линия 2
penup()
goto(-50,-175)
pendown()
goto(-50,270)
penup()

#
#
#

mainloop()