def figyra_kon(x1, y1, x2, y2):
    return abs(abs(x1 - x2) - abs(y1 - y2)) == 1


def main():
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    if figyra_kon(x1, y1, x2, y2):
        print('Yes')
    else:
        print('No')

main()