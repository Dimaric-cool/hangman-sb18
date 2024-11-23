import string
import turtle
from multiprocessing.connection import default_family
from turtle import *

WIDTH = 800
HEIGHT = 700
secret = "черепашка"

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

def draw_squares(secretWord):
    secretCoords = {}
    dlinakwadr = 50
    otstup = 20
    X = - (len(secretWord) * dlinakwadr + (len(secretWord) - 1) * otstup) // 2
    Y = -250

    for letter in secretWord:
        goto(X, Y)
        if letter not in secretCoords:
            secretCoords[letter] = [(X + dlinakwadr // 2, Y - dlinakwadr)]
        else:
            secretCoords[letter].append((X + dlinakwadr // 2, Y - dlinakwadr))
        pendown()
        for _ in range(4):
            forward(dlinakwadr)
            right(90)
        penup()
        X += dlinakwadr + otstup
    return secretCoords

def draw_letter(letter, coords, penColor = "black"):
    color(penColor)
    goto(coords)
    write(letter, False, "center", ("Comic Sans MS", fontSize, "bold"))

def draw_alphabet(coords):
    X, Y = coords
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphaCoords = {}
    for letter in alphabet:
        alphaCoords[letter] = (X, Y)
        draw_letter(letter, (X, Y))
        X += 60
        if X >= 350:
            X = 70
            Y -= 65
    return alphaCoords

def get_coord(x, y):
    click_check((x, y))

def click_check(coord):
    global alphaCoords
    d = fontSize // 2
    for key, value in alphaCoords.items():
        if abs(coord[0] - value[0]) <= d and abs((coord[1]) - (value[1] + d)) <= d :
            draw_letter(key, value, "grey")
            del alphaCoords[key]
            letter_check(key)
            return

def letter_check(letter):
    if letter in secretCoords:
        for coord in secretCoords[letter]:
            draw_letter(letter, coord, "green")

# Отрисовка квадратов для загаданного слова
secretCoords = draw_squares(secret)

# Отрисовка виселицы
for error in range(1, 11):
    draw_error(error)

# Отрисовка алфавита
alphaCoords = draw_alphabet((70, 210))

# Обработка кликов по алфавиту
Screen().onclick(get_coord)

mainloop()
