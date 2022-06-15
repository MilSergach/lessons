"""Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""
from classwork_04 import Animal


class Cat(Animal):

    def meow(self):
        print(self.name, 'meowing')


if __name__ == '__main__':
    cat1 = Cat(5, 3, 'cat1', 4)
    cat1.prints()
    cat1.meow()
