import random
import turtle

# Список слов
words = ["попугай", "телефон", "праграма", "лень", "частота", "вавля"]

# Случайный выбор слова
secret_word = random.choice(words)
guessed_letters = []  # Угаданные буквы
mistakes = 0  # Количество ошибок
max_mistakes = 6  # Максимум ошибок

# Настройка экрана
screen = turtle.Screen()
screen.title("Игра Виселица")
screen.setup(width=600, height=600)

# Создание холста для рисования
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
# Функция для рисования виселицы и частей тела



def draw_hangman(mistakes):
    if mistakes == 1:  # Основание
        pen.penup()
        pen.goto(-100, -200)
        pen.pendown()
        pen.forward(200)
    elif mistakes == 2:  # Столб
        pen.penup()
        pen.goto(-50, -200)
        pen.pendown()
        pen.goto(-50, 100)
    elif mistakes == 3:  # Перекладина
        pen.goto(50, 100)
    elif mistakes == 4:  # Веревка
        pen.goto(50, 50)
    elif mistakes == 5:  # Голова
        pen.penup()
        pen.goto(50, 25)
        pen.pendown()
        pen.circle(25)
    elif mistakes == 6:  # Тело
        pen.penup()
        pen.goto(50, 25)
        pen.pendown()
        pen.goto(50, -50)
    elif mistakes == 7:  # Рука левая
        pen.goto(30, 0)
    elif mistakes == 8:  # Рука правая
        pen.penup()
        pen.goto(50, -25)
        pen.pendown()
        pen.goto(70, 0)
    elif mistakes == 9:  # Нога левая
        pen.penup()
        pen.goto(50, -50)
        pen.pendown()
        pen.goto(30, -100)
    elif mistakes == 10:  # Нога правая
        pen.penup()
        pen.goto(50, -50)
        pen.pendown()
        pen.goto(70, -100)

        # Функция для отображения текущего состояния слова
        def display_word():
            pen.penup()
            pen.goto(-200, 200)
            pen.pendown()
            display = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    display += letter + " "
                else:
                    display += "_ "
            pen.clear()
            pen.write(display, font=("Arial", 24, "normal"))

            # Обработка нажатий клавиш
            def key_press(key):
                if key.isalpha() and len(key) == 1:
                    check_letter(key.lower())

            # Установка обработчика событий для клавиатуры
            screen.listen()
            for letter in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
                screen.onkey(lambda l=letter: key_press(l), letter)

            # Отображение начального состояния
            display_word()

            # Запуск игрового цикла
            screen.mainloop()
