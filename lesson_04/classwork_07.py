my_list1 = []
my_list2 = []
my_list3 = []
my_list = []
itog = []
while True:
    x = input('Vvedite chislastroki 1 : ')
    try:
        my_number = int(x)
        my_list1.append(my_number)
    except ValueError:
        break

while True:
    x = input('Vvedite chislo stroki 2 : ')
    try:
        my_number = int(x)
        my_list2.append(my_number)
    except ValueError:
        break

while True:
    x = input('Vvedite chisla stroki 3 : ')
    try:
        my_number = int(x)
        my_list3.append(my_number)
    except ValueError:
        break

for i in my_list1:
    for k in my_list2:
        if i == k:
            my_list.append(i)
for k in my_list:
    for u in my_list3:
        if k == u:
            my_list.remove(k)
print(my_list)
