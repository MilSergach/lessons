n = input()
my_list = [n]
for i in reversed(my_list):
    for k in my_list:
        if i == k:
            print('yes')