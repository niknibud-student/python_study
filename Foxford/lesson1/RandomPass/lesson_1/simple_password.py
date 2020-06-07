from random import choice, sample
letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
numbers = [str(i) for i in range(10)]
list_of_elements = letters + numbers

length = 10

password_list = [choice(list_of_elements) for i in range(length)]
print(password_list)

password_list = sample(list_of_elements, k=length)
print(password_list)

password = ''
password = ''.join(password_list)
print(password)