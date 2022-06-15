"""Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать
Dog и Cat от класса Animal и Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы."""


class Animal:
    height = None
    weight = None
    name = None
    age = None

    def __init__(self, heigt: int, weight: int, name: str, age: int):
        self.height = heigt
        self.weight = weight
        self.name = name
        self.age = age

    def prints(self):
        print('Name:', self.name)
        print('Weight:', self.weight)
        print('Height:', self.height)
        print('Age:', self.age)

    def jump(self):
        print(self.name, 'jumping')

    def run(self):
        print(self.name, 'running')


class Dog(Animal):

    def bark(self):
        print(self.name, 'barking')


class Cat(Animal):

    def meow(self):
        print(self.name, 'meowing')


if __name__ == '__main__':
    dog1 = Dog(25, 13, 'Bob', 15)
    dog1.bark()
    dog1.jump()
    dog1.run()
    cat1 = Cat(12, 10, 'CaT', 10)
    cat1.meow()
    cat1.jump()
    cat1.run()
