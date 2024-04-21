#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class Triad(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def increment(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Triad):
            raise NotImplementedError
        return self.a == other.a and self.b == other.b and self.c == other.c


class Date(Triad):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    def increment(self):
        if self.b in [1, 3, 5, 7, 8, 10, 12]:
            days_in_month = 31
        elif self.b in [4, 6, 9, 11]:
            days_in_month = 30
        elif self.b == 2:

            if (self.a % 4 == 0 and self.a % 100 != 0) or (self.a % 400 == 0):
                days_in_month = 29
            else:
                days_in_month = 28
        else:
            raise ValueError("Некорректный месяц")

        self.c += 1

        if self.c > days_in_month:
            self.c = 1
            self.b += 1

            if self.b > 12:
                self.b = 1
                self.a += 1

    def __lt__(self, other):
        return (self.a, self.b, self.c) < (other.a, other.b, other.c)

    def __le__(self, other):
        return (self.a, self.b, self.c) <= (other.a, other.b, other.c)

    def __gt__(self, other):
        return (self.a, self.b, self.c) > (other.a, other.b, other.c)

    def __ge__(self, other):
        return (self.a, self.b, self.c) >= (other.a, other.b, other.c)


class Time(Triad):
    def __init__(self, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)

    def increment(self):
        self.c += 1
        if self.c >= 60:
            self.c = 0
            self.b += 1
            if self.b >= 60:
                self.b = 0
                self.a += 1
                if self.a >= 24:
                    self.a = 0


def demonstrate_virtual_call(triad):
    triad.increment()
    print(f"Triad after increment: {triad.a}, {triad.b}, {triad.c}")


if __name__ == "__main__":
    date1 = Date(2020, 1, 31)
    date2 = Date(2020, 2, 1)
    time1 = Time(23, 59, 59)

    demonstrate_virtual_call(date1)
    demonstrate_virtual_call(time1)

    print(f"date1 < date2: {date1 < date2}")
    print(f"date1 > date2: {date1 > date2}")
