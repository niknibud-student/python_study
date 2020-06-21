

# Функция для шифровки
def encrypt(list_of_symbols_from_text):
    list_of_codes_of_symbols = []


# Функция для дешифровки
def decrypt(text):
    pass






print('Зашифровать(1) или расшифровать(2) сообщение? Введите 1 или 2:')
answer = input()
print('Введите текст:')
text = input()
length = len(text)
list_of_symbols_from_text = list(text)

[list_of_symbols_from_text.append(text[i]) for i in range(length)]
