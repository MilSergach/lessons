"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли
ледующую карту, в случае положительного ответа  - вытягивать случайную карту. Игра
заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""
from classwork_03 import get_random_card

my_dict = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 1, 'D': 2, 'K': 3, 'A': 4}
def nominal_to_value(nominal):
    return my_dict[nominal]


n, _ = get_random_card()
value = nominal_to_value(n)
current_sum = value

while True:
    choice = input("Достать следующую карту [Y/n]: ")
    if choice == 'n':
        break

    n, _ = get_random_card()
    value = nominal_to_value(n)
    current_sum += value

    if current_sum > 21:
        print("Game over", current_sum)
        break

    if current_sum == 21:
        print("You WIN!", current_sum)
        break

    if current_sum < 21:
        print("You score: ", current_sum)