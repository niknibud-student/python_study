import random
length = 4
numbers = [random.randrange(1, 10) for i in range(length)]
#for i in range(length):
#    numbers.append(random.randrange(1, 10))
print(*numbers)