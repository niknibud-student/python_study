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
