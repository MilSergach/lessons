def three_args(arym):
    if len(arym) == 1:
        print('var1 = ', arym[0])
    if len(arym) == 2:
        print('var1 = ', arym[0], 'var2 = ', arym[1])
    if len(arym) == 3:
        print('var1 = ', arym[0], 'var2 = ', arym[1], 'var3 = ', arym[2])
    if len(arym) == 0 or len(arym) > 3:
        print('Error')


my_list = [1 , 235]
three_args(my_list)
