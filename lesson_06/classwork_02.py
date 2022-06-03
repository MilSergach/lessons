import csv

my_dict = {}

with open("dictionary.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       my_dict[row[0]] = row[1]
       my_dict = {row[0]: row[1] for row in csv.reader(file)}

def eng_to_rus(word):
    return my_dict[word]


def rus_to_eng(word):
    for key, value in my_dict.items():
        if value == word:
            return key

def rus_to_engg(word):
    new_dict = {
        value: key
        for key, value in my_dict.items()
    }
    return my_dict[word]




print(eng_to_rus("apple"))
print(eng_to_rus("green"))
print(eng_to_rus("fly"))

print(rus_to_engg("яблоко"))