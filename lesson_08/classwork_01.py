"""Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты"""

from classwork_04 import Animal


class Dog(Animal):

    def bark(self):
        print(self.name, 'barking')
3

if __name__ == '__main__':
    dog = Dog(32, 48, 'Bob', 22)
    dog.prints()
    dog.jump()
    dog.run()
    dog.bark()
