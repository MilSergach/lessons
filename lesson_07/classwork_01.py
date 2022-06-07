def is_figures_beat(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 -y2)

def main():
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    if is_figures_beat(x1, y1, x2, y2):
        print('Yes')
    else:
        print('No')

main()