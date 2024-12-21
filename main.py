from turtle import *

import words

WIDTH = 800
HEIGHT = 700
secret = ""

Screen()._root.iconbitmap("logo.ico")
title("Hangman GAME")
Screen().setup(WIDTH, HEIGHT)
hideturtle()

speed(0)

fontSize = 42
pensize(10)

countErrors = 0
countLetters = 0
secretCoords = {}
alphaCoords = {}
buttonCoords = {}

def startGame():
    global secret
    global countLetters
    global countErrors
    global secretCoords
    global alphaCoords
    global buttonCoords

    clear()

    secret = words.randomWord()
    countLetters = len(secret)
    countErrors = 0
    penup()
    color("black")
    buttonCoords = {}
    # Отрисовка квадратов для загаданного слова
    secretCoords = draw_squares(secret)

    # Отрисовка алфавита
    alphaCoords = draw_alphabet((70, 210))


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
            goto(-220, 220)
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
            color("black")
            del alphaCoords[key]
            letter_check(key)
            return

    if buttonCoords:
        if abs(coord[0] - buttonCoords["ПОВТОРИТЬ"][0]) <= d*len("ПОВТОРИТЬ") and abs((coord[1]) - (buttonCoords["ПОВТОРИТЬ"][1] + d)) <= d:
            startGame()
            return
        if abs(coord[0] - buttonCoords["ВЫЙТИ"][0]) <= d*len("ВЫЙТИ") and abs((coord[1]) - (buttonCoords["ВЫЙТИ"][1] + d)) <= d:
            bye()
            return


def letter_check(letter):
    global countErrors
    global countLetters
    if letter in secretCoords:
        for coord in secretCoords[letter]:
            draw_letter(letter, coord, "green")
            countLetters -= 1
            # если отгадали все буквы - победа
            if countLetters <= 0:
                end_game()
    else:
        countErrors += 1
        draw_error(countErrors)
        # если набрали 10 ошибок - поражение
        if countErrors >= 10:
            end_game(False)

def end_game(win=True):
    global alphaCoords
    global buttonCoords

    buttonCoords = {"ПОВТОРИТЬ": (-200, -250), "ВЫЙТИ": (200, -250)}

    alphaCoords.clear()
    clear()
    fontColor = "green"
    status = "победили"

    if not win:
        fontColor = "red"
        status = "проиграли"

    goto(0, 210)
    color(fontColor)
    write(f"Вы {status}", False, "center", ("Comic Sans MS", 72, "bold"))
    goto(0, 40)
    color("black")
    write("загаданное слово:", False, "center", ("Comic Sans MS", 40, "bold"))
    goto(0, -50)
    color(fontColor)
    write(secret, False, "center", ("Comic Sans MS", 60, "bold"))
    goto(buttonCoords["ПОВТОРИТЬ"])
    color("green")
    write("ПОВТОРИТЬ", False, "center", ("Comic Sans MS", 42, "bold"))
    goto(buttonCoords["ВЫЙТИ"])
    color("red")
    write("ВЫЙТИ", False, "center", ("Comic Sans MS", 42, "bold"))




startGame()

# Обработка кликов по алфавиту
Screen().onclick(get_coord)

mainloop()
