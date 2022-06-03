my_dict = {
    "apple": "яблоко",
    "green": "зеленый",
    "fly": "летать",
}

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
