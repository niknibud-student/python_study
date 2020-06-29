from tkinter import Tk, Button, DISABLED, Label, messagebox, Canvas
import random
import time


def close_window(self):
    root.destroy()


# Перевернуть карточку
def flip_over(x, y):
    global first, previousX, previousY, attempts
    buttons[x, y]['text'] = button_symbols[x, y]

    if first:
        previousX = x
        previousY = y
    else:
        attempts += 1
        canvas.itemconfigure(number_of_attempts, text='Количество шагов: ' + str(attempts))
        Label(text='Количество шагов: ' + str(attempts)).grid(column=0, row=3)
        root.update()


# Перевернуть карточки, если не угадал
def flip_back(x, y, previousX, previousY):
    buttons[previousX, previousY]['text'] = ''
    buttons[x, y]['text'] = ''


def the_same_button(x, y):
    global previousY, previousY
    return False if previousX != x or previousY != y else True



def buttons_are_guessed(x, y):
    return True if buttons[previousX, previousY]['text'] == buttons[x, y]['text'] else False


def stay_opened(x, y):
    global number_of_guessed_pairs
    buttons[previousX, previousY]['command'] = DISABLED
    buttons[x, y]['command'] = DISABLED
    number_of_guessed_pairs += 1
    if number_of_guessed_pairs == number_of_pairs:
        messagebox.showinfo('Количество ходов', 'Сделано ходов: ' + str(attempts), command=close_window(root))


# Основная функция переворота карточек
def tap(x, y):
    global first, previousX, previousY

    if first:
        flip_over(x, y)
        first = False
    else:
        if not the_same_button(x, y):
            flip_over(x, y)
            if buttons_are_guessed(x, y):
                stay_opened(x, y)
            else:
                root.after(500, flip_back, x, y, previousX, previousY)
            first = True
            previousX, previousY = 0, 0


def choose_difficalty():
    print("Выберите сложность (1, 2 или 3):\n 1 Лёгкий \n 2 Средний \n 3 Сложный ")
    answer = int(input())
    if answer == 1:
        n, m = 4, 2
    elif answer == 2:
        n, m = 6, 4
    elif answer == 3:
        n, m = 8, 6
    else:
        print('Некорректный ответ')
        n, m = 0, 0
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
attempts = 0
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
Label(text=str(attempts)).grid(column=0, row=3)
number_of_attempts = canvas.create_text(125, 10, text='Количество шагов: ' + str(attempts))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        button = Button(width=3, height=3, bg='yellow', text='', command=lambda x=i, y=j: tap(x, y))
        button.grid(column=i, row=j)
        buttons[i, j] = button
        button_symbols[i, j] = symbols_in_game.pop()
root.mainloop()
