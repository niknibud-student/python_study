import string
import random

letters = string.ascii_letters
digits = string.digits
symbol = string.punctuation
str_elements = letters + digits + symbol
random_symbol = random.choice(str_elements)
print(random_symbol)