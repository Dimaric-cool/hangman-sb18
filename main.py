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


def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    penup()

def draw_error(numError):
    match numError:
        case 1:
            draw_line(-350, -175, -30, -175)
        case 2:
            draw_line(-50, -175, -50, 270)
        case 3:
            draw_line(-50, 270, -220, 270)
        case 4:
            draw_line(-220, 270, -220, 220)
        case 5:
            pendown()
            circle(-50)
            penup()
        case 6:
            draw_line(-220, 120, -220, -30)
        case 7:
            draw_line(-220, -30, -130, -130)
        case 8:
            draw_line(-220, -30, -310, -130)
        case 9:
            draw_line(-220, 70, -130, 120)
        case 10:
            draw_line(-220, 70, -310, 120)


mainloop()
