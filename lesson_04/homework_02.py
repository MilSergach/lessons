my_list = input("Vvedite palindrom: ")
my_list1 = list(my_list)
my_list = list(my_list)
my_list.reverse()
if my_list == my_list1:
    print('Yes')
else:
    print('No')
