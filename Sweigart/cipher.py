SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПТСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать (1), расшифровать (2) или взломать (3) текст? Введите 1, 2 или 3.')
        mode = int(input())
        if mode in [1, 2, 3]:
            return mode
        else:
            print('Введите 1, 2 или 3!')

def getMessage():
    print('Введите текст:')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1 - %s)' % MAX_KEY_SIZE)
        key = int(input())

        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslateMessage(mode, mesage, key):
    if mode == 2:
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Символ не найден
            # Просто добавить это символ
            translated += symbol
        else:
            # Зашифровать или расшифровать
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated

mode = getMode()
message = getMessage()

if mode != 3:
    key = getKey()

print('Преобразованный текст:')
if mode != 3:
    print(getTranslateMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslateMessage(2, message, key))
