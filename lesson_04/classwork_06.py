n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
k = 0
my_list = []
for i in range(n, m + 1):
    k += 1
    my_list.append(i)
print(my_list, '\n''Колличество чисел: ', k)
