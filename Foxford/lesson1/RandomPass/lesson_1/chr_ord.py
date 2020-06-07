print(chr(65))
print(chr(97))

letters_from_table = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
print(letters_from_table)

russian_letters = [chr(i) for i in range(ord('А'), ord('Я')+1)] + [chr(i) for i in range(ord('а'), ord('я')+1)]
print(russian_letters)
print(ord('А'), ord('Ё'), ord('а'), ord('ё'))