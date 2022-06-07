import csv

my_dict = {}
my_dict2 = {}

with open('List_base.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        sh = float(row[2]), float(row[3])
        if row[0] in my_dict.keys():
           sh = my_dict.get(row[0])[0] + float(row[2]), my_dict.get(row[0])[1] + float(row[3])
           my_dict[row[0]] = sh
        else:
            my_dict[row[0]] = sh

        pl = float(row[2]), float(row[3]) * float(row[2])
        if row[1] in my_dict2.keys():
            pl = my_dict2.get(row[1])[0] + float(row[2]), my_dict2.get(row[1])[1] + float(row[3]) * float(row[2])
            my_dict2[row[1]] = pl
        else:
            my_dict2[row[1]] = pl

print(my_dict2)

print(my_dict)