# python_study
Изучение Python по различным источникам

### Функция проверки на простоту
Взял отсюда: [Проверка числа на простоту в Python](https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python)
```python
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
```
### Алгоритм определения существования и типа треугольников
В ответ надо вывести целое число: 
* -1, если треугольник с такими сторонами не существует, 
* 0, если треугольник прямоугольный, 
* 1, если треугольник остроугольный и 2, если треугольник тупоугольный.

1) Ищем максимальную сторону, пусть c.
2) Если c >= a + b, то треугольник невозможен
3) Считаем знак `a*a + b*b - c*c`
* +: остроугольный
* 0: прямоугольный
* -: тупоугольный

Мне кажется не лучшее решение
```python
arr = []
for i in range(3):
    arr.append(abs(float(input())))
sorted(arr)
if arr[2] < arr[0] + arr[1]:
    if arr[0]**2 + arr[1]**2 - arr[2]**2 > 0:
        print(1)
    elif arr[0]**2 + arr[1]**2 - arr[2]**2 < 0:
        print(2)
    else:
        print(0)
else:
    print(-1)
```
### Сортировка чисел по сумме их цифр
```python
print(*sorted(input().split(), key=lambda x: sum([int(i) for i in x])))
```
