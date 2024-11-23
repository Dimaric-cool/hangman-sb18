import string
import turtle
from turtle import *

WIDTH = 800
HEIGHT = 700

Screen().setup(WIDTH, HEIGHT)

shape("turtle")
speed(0)
shapesize(1.5)
fontSize = 42
pensize(10)
penup()



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

def draw_squares(dlinaSlova):
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


def draw_alphabet(coords, fontSize):
    X, Y = coords
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphaCoords = {}
    for letter in alphabet:
        alphaCoords[letter] = (X, Y)
        goto(X, Y)
        write(letter, False, "center", ("Comic Sans MS", fontSize, "bold"))
        X += 60
        if X >= 350:
            X = 70
            Y -= 65
    return alphaCoords

def get_coord(x, y):
    click_check((x, y), alphaCoords)

def click_check(coord, dicti):
    d = fontSize // 2
    for key, value in dicti.items():
        if abs(coord[0] - value[0]) <= d and abs((coord[1]) - (value[1] + d)) <= d :
            print(key)

draw_squares(6)

for error in range(1, 11):
    draw_error(error)

alphaCoords = draw_alphabet((70, 210), fontSize)


Screen().onclick(get_coord)
mainloop()
