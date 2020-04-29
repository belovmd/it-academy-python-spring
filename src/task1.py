# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
# покупка билета в транспортной компании, или простая РПГ. Создайте несколько
# объектов классов, которые описывают ситуацию Объекты должны содержать как
# атрибуты так и методы класса для симуляции различных действий. Программа
# должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
# методы, взаимодействие объектов и т.д.

# The Defenders
# In the previous mission - Army battles, you've learned how to make a
# battle between 2 armies. But we have only 2 types of units - the Warriors
# and Knights. Let's add another one - the Defender. It should be the subclass
# of the Warrior class and have an additional defense parameter, which helps
# him to survive longer. When another unit hits the defender, he loses a
# certain amount of his health according to the next formula: enemy attack -
# self defense (if enemy attack > self defense). Otherwise, the defender
# doesn't lose his health.


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, number):
        for _ in range(number):
            self.units.append(unit())


class Battle:
    @staticmethod
    def fight(army1, army2):
        while army1.units and army2.units:
            if army1.units[-1].attack > army2.units[0].defense:
                army2.units[0].health -= \
                    (army1.units[-1].attack - army2.units[0].defense)
            if army2.units[0].health <= 0:
                army2.units.pop(0)
                continue
            if army2.units[0].attack > army1.units[-1].defense:
                army1.units[-1].health -= \
                    (army2.units[0].attack - army1.units[-1].defense)
            if army1.units[-1].health <= 0:
                army1.units.pop(-1)
        return True if army1.units else False


def fight(unit_1, unit_2):
    while True:
        if unit_1.attack > unit_2.defense:
            unit_2.health -= (unit_1.attack - unit_2.defense)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        if unit_2.attack > unit_1.defense:
            unit_1.health -= (unit_2.attack - unit_1.defense)
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True

    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
    print("Coding complete? Let's try tests!")
