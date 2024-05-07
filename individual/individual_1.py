#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 10
# Создать класс Triad (тройка чисел); определить метод сравнения триад (см. задание 2).
# Определить производный класс Date с полями: год, месяц и день. Определить полный набор
# методов сравнения дат.


class Triad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        if not isinstance(other, Triad):
            raise NotImplementedError
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __lt__(self, other):
        if not isinstance(other, Triad):
            raise NotImplementedError
        return (self.a, self.b, self.c) < (other.a, other.b, other.c)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other


class Date(Triad):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    def __repr__(self):
        return f"Date({self.a}, {self.b}, {self.c})"


if __name__ == "__main__":
    # Тестирование класса Triad
    triad1 = Triad(1, 2, 3)
    tread2 = Triad(1, 2, 3)

    assert triad1 == triad1, "Triad1 должен быть равен Triad2"

    # Тестирование класса Date
    date1 = Date(2020, 1, 1)
    date2 = Date(2020, 1, 2)
    date3 = Date(2020, 1, 1)
    date4 = Date(2021, 1, 1)

    assert date1 < date2, "date1 должна быть меньше date2"

    assert date1 <= date3, "date1 должна быть меньше или равна date3"
    assert date1 <= date2, "date1 должна быть меньше date2"

    assert date1 == date3, "date1 должна быть равна date3"

    assert date1 != date4, "date1 не должна быть равна date4"

    assert date4 > date3, "date4 должна быть больше date3"

    assert date4 >= date1, "date4 должна быть больше или равна date1"
    assert date1 >= date3, "date1 должна быть больше или равна date3"

    print("Все тесты пройдены успешно!")
