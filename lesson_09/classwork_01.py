"""Создать класс MyTime. Атрибуты: hours, minutes,
 secondsМетоды: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""

from __future__ import annotations


class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_sec(self):
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

    def __eq__(self, other: MyTime):
        return self.to_sec() == other.to_sec()

    def __ne__(self, other: MyTime):
        return self.to_sec() != other.to_sec()

    def __lt__(self, other: MyTime):
        return self.to_sec() < other.to_sec()

    def __gt__(self, other: MyTime):
        return self.to_sec() > other.to_sec()

    def __le__(self, other: MyTime):
        return self.to_sec() <= other.to_sec()

    def __ge__(self, other: MyTime):
        return self.to_sec() >= other.to_sec()


if __name__ == '__main__':
    a = MyTime(3, 25, 35)
    d = MyTime(2, 85, 35)
    print(a == d)