#!/usr/bin/env python
# -*- coding: utf-8 -*-

# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
# номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
# метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
# героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле
# генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
# героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
# идентификационные номера этих двух юнитов.


from random import randint


class Person:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Soldier(Person):
    def __init__(self, id, team):
        super().__init__(id, team)
        self.hero = None

    def go_to_hero(self, hero):
        self.hero = hero


class Hero(Person):
    def __init__(self, id, team):
        super().__init__(id, team)
        self.level = 1

    def up_level(self):
        self.level += 1


def main():
    hero_A = Hero(1, "A")
    hero_B = Hero(2, "B")

    lst_A = []
    lst_B = []
    for i in range(100):
        team = randint(1, 2)
        if team == 1:
            lst_A.append(Soldier(i, "A"))
        else:
            lst_B.append(Soldier(i, "B"))

    print(f'В команде "A" находится {len(lst_A)} солдат')
    print(f'В команде "B" находится {len(lst_B)} солдат')

    # Увеличение уровня героя у команды, в которой больше солдат
    if len(lst_A) >= len(lst_B):
        hero_A.up_level()
        lst_A[0].go_to_hero(hero_A)
        print(hero_A.id, lst_A[0].id)
    else:
        hero_B.up_level()
        lst_B[0].go_to_hero(hero_B)
        print(hero_B.id, lst_B[0].id)


if __name__ == "__main__":
    main()
