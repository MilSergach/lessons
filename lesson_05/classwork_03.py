my_args = []
func_type = input('min or max: ')
while True:
    k = input('Vvedite chisla: ')
    try:
        i = int(k)
        my_args.append(i)
    except ValueError:
        break

def func_max(*args):
    max_value = args[0]
    for y in my_args:
        if y > max_value:
            max_value = y
    return max_value

def func_min(*args):
    min_value = args[0]
    for t in my_args:
        if t < min_value:
            min_value = t
    return min_value

def min_or_max(func_type,*args):
    if func_type == 'min':
        result = func_min(*args)
    else:
        result = func_max(*args)
    return result

print(min_or_max(func_type, *my_args))