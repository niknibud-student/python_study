# Игра Виселица

import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[O   |
/|\  |
/ \  |
    ===''', '''
 +---+
[O] |
/|\ |
/ \ |
   ===''']

words =  {'Цвета':'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
          'Фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
          'Фрукты':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
          'Животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит \
кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск \
моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака \
сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()}


# Эта функция возвращает случайную строку из переданного списка.
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey


# Функция печатает виселицу и шаблон для секретного слова
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')

    print()


# Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
def getGuess(alreadyGuessed):
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


# Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')

difficulty = ' '
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый')
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = '' # Пропущенные буквы
correctLetters = '' # Правильные буквы
secretWord, secretSet = getRandomWord(words) # Загаданное слово
gameIsDone = False

while True:
    print('Секретное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess # Собирает угаданные буквы

        # Проверяет, выиграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)

            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
