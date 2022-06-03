klass1 = int(input("Kol-vo ychashihsa v 1 klasse:"))
klass2 = int(input("Kol-vo ychashihsa v 2 klasse:"))
klass3 = int(input("Kol-vo ychashihsa v 3 klasse:"))

def parta(x, y, z):
    all_stud = klass1 + klass2 + klass3
    tables = all_stud / 2
    if tables == float(tables):
        tables += 0.5
        print('Вам необходимо :', int(tables), 'парт')
    else:
        print('Вам необходимо :', tables, 'парт')

parta(klass1, klass2, klass3)