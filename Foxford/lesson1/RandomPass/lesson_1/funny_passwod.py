import random
import string

password = ''
adjectives = ['смешных', 'полосатых', 'маленьких', 'хрустальных', 'чёрных', 'радостных', 'медленных', 'фиолетовых']
nouns = ['слонов', 'бегемотов', 'крокодилов', 'обезьян', 'драконов', 'котиков', 'единорогов', 'пегасов', 'лягушек']
verbs = ['бегут', 'летят', 'прыгают', 'читают', 'хрюкают']

noun = random.choice(nouns)
adjective = random.choice(adjectives)
verb = random.choice(verbs)
numbers = str(random.randrange(2, 100))
symbol = random.choice(string.punctuation)
password = numbers + adjective + noun + verb + symbol
print(password)