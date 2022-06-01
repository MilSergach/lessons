my_args = []

while True:
    r = input('Vvedite chislo: ')
    try:
        new = int(r)
        my_args.append(new)
    except ValueError:
        break

def sum_and_max(*args):
    result_sum = 0
    max_value = 0
    for i in args:
        result_sum += i
        if i > max_value:
            max_value = i
    return result_sum, max_value

print(sum_and_max(*my_args))
