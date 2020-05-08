"""Создайте  модель из жизни. Это может быть
бронирование комнаты в отеле, покупка билета
в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые
описывают ситуацию Объекты должны содержать
как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать
объекты и эмулировать какую-либо ситуацию - вызывать
методы, взаимодействие объектов и т.д.

Часть TBS - битва космических флотов."""


import random


class StarFleet:
    def __init__(self, empire, coalition, name, corvette, destroyer, cruiser, battleship):
        self.empire = empire
        self.coalition = coalition
        self.name = name
        self.corvette = corvette
        self.destroyer = destroyer
        self.cruiser = cruiser
        self.battleship = battleship
        print("Fleet %s of %s Empire arrive in the system!" % (name, empire))


class SpaceBattle:
    def __init__(self, battle):
        self.fleets = list()
        self.battle = battle

    def deployment(self, starfleet):
        self.fleets.append(starfleet)

    def retreat(self, starfleet):
        self.fleets.remove(starfleet)

    @staticmethod
    def calc_damage(a, bb, ca):
        a.corvette -= random.uniform(3.0, 10 * (bb / ca))
        a.destroyer -= random.uniform(1.0, 5 * (bb / ca))
        a.cruiser -= random.uniform(0.3, 2 * (bb / ca))
        a.battleship -= random.uniform(0.15, 1 * (bb / ca))

    def friend_or_foe(self):
        coalitions = {element.coalition for element in self.fleets}
        if len(self.fleets) > 0 and len(coalitions) > 1:
            spacebattle.attack()

        elif len(self.fleets) == 0:
            print("Now no fleets in the system.")
            quit()

        elif len(coalitions) == 1:
            print("No enemies in the system.")
            print("Forces of %s coalition occupied the system!" % list(coalitions)[0])
            quit()

    def attack(self):
        """Choose fleet that will strike first"""
        first = random.choice(self.fleets)
        print("Attack of %s fleet!" % first.name)
        """List of fleets not in first's coalition"""
        enemies = [element for element in self.fleets if first.coalition != element.coalition]
        """Choose target for first fleet"""
        second = random.choice(enemies)
        print("%s fleet under attack!" % second.name)

        first_strength = first.corvette + first.destroyer * 2 + first.cruiser * 4 + first.battleship * 8
        second_strength = second.corvette + second.destroyer * 2 + second.cruiser * 4 + second.battleship * 8

        """Check balance of strength and morality = random.random()"""
        if (second_strength < 0.5 * first_strength) and random.random() < 0.8:
            spacebattle.retreat(second)
            print("Fleet %s are retreat!" % second.name)
        elif (first_strength < 0.5 * second_strength) and random.random() < 0.8:
            spacebattle.retreat(first)
            print("Fleet %s are retreat!" % first.name)
        else:
            """Calculate damage. Float type means that some ships can be damaged, but they can still fight"""

            self.calc_damage(second, first_strength, second_strength)

            print("Counterattack of %s fleet!" % second.name)

            self.calc_damage(first, second_strength, first_strength)

            """Remove destroyed types of ships"""
            for number in range(0, len(self.fleets)):
                for el in self.fleets[number].__dict__:
                    if isinstance(self.fleets[number].__dict__[el], float):
                        if self.fleets[number].__dict__[el] < 0:
                            self.fleets[number].__dict__[el] = 0

            """Check relative strength of fleets after strikes"""
            first_strength = first.corvette + first.destroyer * 2 + first.cruiser * 4 + first.battleship * 8
            print(first.name, round(first_strength, 2))
            second_strength = second.corvette + second.destroyer * 2 + second.cruiser * 4 + second.battleship * 8
            print(second.name, round(second_strength, 2))

        """Check result of strikes"""
        if first_strength <= 0 and second_strength <= 0:
            spacebattle.retreat(first)
            spacebattle.retreat(second)
            print("Fleets destroyed!")
        elif first_strength <= 0:
            spacebattle.retreat(first)
            print("Fleet %s are destroyed!" % first.name)
        elif second_strength <= 0:
            spacebattle.retreat(second)
            print("Fleet %s are destroyed!" % second.name)
        elif first_strength < second_strength * 0.25 and first in self.fleets:
            spacebattle.retreat(first)
            print("Fleet %s is running!" % first.name)
        elif second_strength < first_strength * 0.25 and second in self.fleets:
            spacebattle.retreat(second)
            print("Fleet %s is running!" % second.name)

        print("Fleets in the system:")
        for el in self.fleets:
            print(el.name, round(el.corvette, 2), round(el.destroyer, 2), round(el.cruiser, 2), round(el.battleship, 2))


if __name__ == '__main__':
    fleet_1 = StarFleet('Arr', "Arr-C", 'Arr-1', 50.0, 20.0, 10.0, 5.0)
    fleet_2 = StarFleet('Brr', "Brr-C", 'Brr-1', 60.0, 25.0, 8.0, 4.0)
    fleet_3 = StarFleet('Crr', "Crr-C", 'Crr-1', 40.0, 15.0, 12.0, 6.0)
    # fleet_1 = StarFleet('Arr', "Arr-C", 'Arr-1', 1.0, 1.0, 1.0, 1.0)
    # fleet_2 = StarFleet('Brr', "Brr-C", 'Brr-1', 1.0, 1.0, 1.0, 1.0)

    spacebattle = SpaceBattle("Battle in System 1234")

    spacebattle.deployment(fleet_1)
    spacebattle.deployment(fleet_2)
    spacebattle.deployment(fleet_3)

    while True:
        spacebattle.friend_or_foe()
