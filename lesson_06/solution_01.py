text = input('Vvedite tekst: ')
my_list = text.split()
n = 0
r = 1
my_list2 = []
for i in my_list:
    y = 0
    t = len(i)
    if n < t:
        n = t
    for k in my_list:
        if k == i:
            y += 1
            if y > r:
                r += 1

for t in my_list:
    y = 0
    if len(t) == n:
        print('Самое длинное слово: ', t)
        for k in my_list:
            if k == i:
                y += 1
                if y == r:
                    my_list2.append(i)
print('Самое часто встречающееся слово: ', my_list2,'\n', 'Было использованно: ', r, 'раз')
