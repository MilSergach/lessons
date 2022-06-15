"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы:
 увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
  отображение скорости, задний ход (изменение знака скорости)."""


class Car:
    brand = None
    model = None
    year = None
    speed = 0

    def __init__(self, brand: str, model: str, year: int, speed: int = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def prints(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

    def add_speed(self):
        self.speed += 5
        print("speed:", self.speed)

    def sub_speed(self):
        if self.speed > 1:
            self.speed -= 5
        print("speed:", self.speed)

    def stop(self):
        while self.speed != 0:
            self.speed -= 5
            print('speed:', self.speed)

    def my_speed(self):
        print('speed:', self.speed)

    def reverse(self):
        if self.speed == 0:
            self.speed -= 5
            print('speed:', self.speed)


if __name__ == '__main__':
    car1 = Car('Audi', '100', 1990)
    car1.prints()
    car1.add_speed()
    car1.add_speed()
    car1.stop()
    car1.reverse()
