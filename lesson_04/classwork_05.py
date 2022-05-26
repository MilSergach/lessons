n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
x = 0
for result in range(n, m):
    k = result**3
    if k != 0:
        x += k
print(x)