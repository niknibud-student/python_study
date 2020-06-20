n = int(input())
beautiful = False
a = []
for i in range(n):
    a.append(int(input()))
for i in range(1, n - 1):
    if a[i] == (a[i - 1] + a[i + 1]) / 2:
        beautiful = True
if beautiful:
    print('YES')
else:
    print('NO')