from tkinter import Tk, Button, DISABLED, Label, messagebox, Canvas
import random
import time


def close_window(self):
    root.destroy()


# Перевернуть карточку
# todo Заменить название на flip_over
def show(x, y):
    global first, previousX, previousY, moves, label1
    buttons[x, y]['text'] = button_symbols[x, y]

    if first:
        previousX = x
        previousY = y
    else:
        moves += 1
        canvas.itemconfigure(number_of_moves, text='Количество шагов: ' + str(moves))
        label1 = Label(text='Количество шагов: ' + str(moves)).grid(column=0, row=3)
        root.update()
        

# todo Заменить название на flip_back
def close():
    pass


def the_same_button(x, y):
    pass


def buttons_are_guessed(x, y):
    pass


def stay_opened(x, y):
    pass


# Основная функция переворота карточек
def tap(x, y):
    global first, previousX, previousY

    if first:
        show(x, y)
        first = False
    else:
        if not the_same_button(x, y):
            show(x, y)
            if buttons_are_guessed(x, y):
                stay_opened(x, y)
            else:
                root.after(500, close, x, y, previousX, previousY)
            first = True
            previousX, previousY = 0, 0


def choose_difficalty():
    n = 4
    m = 4
    return n, m


# Словарь для координат всех кнопок
buttons = {}
# Флаг для проверки, первый это символ в паре
first = True
second = False
# Координаты предыдущей карточки
previousX = 0
previousY = 0
# Количество угаданных пар
number_of_guessed_pairs = 0
# Количество попыток
# todo Заменить переменную на attemp
moves = 0
# Словарь связка кнопок с символами
button_symbols = {}

canvas_width = 250
canvas_height = 20

# Символы для игры
all_symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709', u'\u2709', u'\u270A', \
               u'\u270A', u'\u270B', u'\u270B', u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712', \
               u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728', u'\u2747', u'\u2747', u'\u274C', \
               u'\u274C', u'\u274E', u'\u274E', u'\u2753', u'\u2753', u'\u2754', u'\u2754', u'\u2755', u'\u2755', \
               u'\u2757', u'\u2757', u'\u2764', u'\u2764', u'\u2795', u'\u2795', u'\u2797', u'\u2797', u'\u27A1', \
               u'\u27A1', u'\u27B0', u'\u27B0']

n, m = choose_difficalty()
symbols_in_game = all_symbols[:(n * m)]
number_of_pairs = n * m // 2

# Создаем окно с заголовком "Memory"
root = Tk()
root.title('Игра Memory')
# Делаем размер окна неизменяемым
root.resizable(width=False, height=False)
random.shuffle(symbols_in_game)

canvas = Canvas(root, width=canvas_width, height=canvas_height)
# Помещаем холст в окно
canvas.grid(column=0, row=1)

Label(text='Игра Мемори').grid(column=0, row=0)
Label(text='Найдите пару одиноковых карточек').grid(column=0, row=2)
label1 = Label(text=str(moves)).grid(column=0, row=3)

number_of_moves = canvas.create_text(125, 10, text='Количество шагов: ' + str(moves))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        button = Button(width=3, height=3, bg='yellow', text='', command=lambda x=i, y=j: tap(x, y))
        button.grid(column=i, row=j)
        buttons[i, j] = button
        button_symbols[i, j] = symbols_in_game.pop()
root.mainloop()
