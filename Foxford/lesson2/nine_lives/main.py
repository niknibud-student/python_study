# Игра "9 жизней"

import random


# Выбор сложности (от 1 - лёгкий до 3 - сложный)
def choose_difficulty():
    print('Выберите сложность: 1, 2 или 3:\n 1 - лёгкий\n 2 - средний\n 3 - сложный')
    answer = int(input())
    return 9 if answer == 1 else 5 if answer == 2 else 3 if answer == 3 else print("Ответ некорректный")


# Вывод количества жизни
def print_num_of_lives():
    global lives
    symbol_of_heart = u'\u2764'
    print(symbol_of_heart * lives)


# Проверяем, угадывали ли уже эту букву
def check_letter_not_guessed_yet(clue, attempt):
    if clue.count(attempt) == 0:
        return True
    else:
        return False


# Попытка угадать букву
def attempt_guess_letter():
    global num_unknown_letters, num_guessed_letters, attmept

    print_num_of_lives()
    print('Угадай букву')

    attempt = input()[0].lower()
    if check_letter_not_guessed_yet(clue, attempt):
        num_guessed_letters += hidden_word.count(attempt)
        num_unknown_letters = len_hidden_word - num_guessed_letters



# Загадываемые слова
words = ['слон', 'бегемот', 'крокодил', 'пегас', 'единорог', 'дракон', 'кентавр', 'котик']

# Угадываемая буква
attmept = ''

# Признак продолжения игры
continue_game = True

# Игра
while continue_game:
    # Количество жизней
    lives = choose_difficulty()
    # Загаданное слово
    hidden_word = random.choice(words)
    len_hidden_word = len(hidden_word)
    num_unknown_letters = len_hidden_word
    # Подсказка
    clue = ['?'] * len_hidden_word
    print(hidden_word)
    print(clue)
    guessed = False
    while lives > 0 and not guessed:
        num_guessed_letters = len_hidden_word - num_unknown_letters
        attempt_guess_letter()