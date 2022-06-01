import random
list_name = ['Alex', 'Olga', 'Anna', 'Irina', 'Serg', 'Alesya', 'Kostek', 'Oleg']
list_name2 = ['Alex', 'Olga', 'Anna', 'Irina', 'Serg', 'Alesya', 'Kostek', 'Oleg']

while True:
     try:
         name1 = random.choice(list_name)
         name2 = random.choice(list_name2)
     except IndexError:
         continue
     if name1 != name2:
            list_name.remove(name1)
            list_name2.remove(name2)
            print(name1, name2)