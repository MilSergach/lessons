"""Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут
имени у объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя. """

from classwork_04 import Animal


class NewDog(Animal):

    def change_name(self, new_name):
        self.name = new_name
        print('New name:', new_name)


if __name__ == '__main__':
    dog = NewDog(10, 15, 'bob', 12)
    dog.prints()
    dog.change_name('Pups')
    dog.prints()