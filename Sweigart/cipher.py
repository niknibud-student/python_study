SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПТСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать (1) или расшифровать (2) текст? Введите 1 или 2.')
        mode = int(input())
        if mode in [1, 2]:
            return mode
        else:
            print('Введите 1 или 2!')

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
key = getKey()

print('Преобразованный текст:')
print(getTranslateMessage(mode, message, key))
