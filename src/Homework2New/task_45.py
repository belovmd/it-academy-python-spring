# This code init battle between two armies
# consist from units with different classes
# with parent class Warrior for all of them.
# Every unit has specific method of attack and defend
# The result of this code is checking which army is alive after battle


class Warrior(object):
    """Warrior class

    Two parameters in class constructor: health and attack
    One property is_alive if health parameter > 0
    """

    def __init__(self, health=50, attack=5):
        """Init parameters of Warrior"""
        self.health = health
        self.attack = attack
        self.start_health = health

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    """Sub class of Warrior class with own parameter values in constructor"""

    def __init__(self, health=50, attack=7):
        Warrior.__init__(self, health, attack)


class Defender(Warrior):
    """Sub class of Warrior class with added defend parameter"""

    def __init__(self, health=60, attack=3, defense=2):
        Warrior.__init__(self, health, attack)
        self.defense = defense


class Vampire(Warrior):
    """Sub class of Warrior class with added vampirism parameter"""

    def __init__(self, health=40, attack=4, vampirism=50):
        Warrior.__init__(self, health, attack)
        self.vampirism = vampirism


class Lancer(Warrior):
    """Sub class from Warrior class with own parameters

    Will have different way to attack enemy
    """

    def __init__(self, health=50, attack=6):
        Warrior.__init__(self, health, attack)


class Healer(Warrior):
    """Sub class from Warrior class

    attack = 0
    health = 60
    Has unique method to increase health of another units
    """
    def __init__(self, health=50, attack=0):
        Warrior.__init__(self, health, attack)

    def heal(self, unit):
        if self.health > 0:
            unit.health = min(unit.start_health, unit.health + 2)


class Army(object):
    """Create army of units from class Warrior or Warrior sub classes"""

    def __init__(self):
        """Init list of units"""
        self.units = []

    def add_units(self, unit, unit_number):
        """Class method 'add_units'

        Add any numbers of units from class Warrior or Knight
        :param unit: unit from class Warrior or Knight
        :param unit_number: number of units
        :return: None
        """
        for _ in range(unit_number):
            self.units.append(unit())


class Battle(object):
    """Init battle between two armies class"""

    def fight(self, army_1, army_2):
        """Class method

        Init fight between two armies while summary health one of them > 0
        :param army_1: list of objects of Warrior or Knight class
        :param army_2: list of object of Warrior or Knight class
        :return: army_1.units[-1].is_alive property
        """

        unit_army1_nmb = unit_army2_nmb = 0

        while unit_army1_nmb < len(army_1.units) and \
                unit_army2_nmb < len(army_2.units):

            if army_1.units[unit_army1_nmb].__class__ == '__main__.Lancer' \
                    and unit_army2_nmb < len(army_2.units) - 1:

                legion_2 = army_2.units[unit_army2_nmb], \
                           army_2.units[unit_army2_nmb + 1]

            else:
                legion_2 = army_2.units[unit_army2_nmb], None

            if army_2.units[unit_army2_nmb].__class__ == '__main__.Lancer' \
                    and unit_army1_nmb < len(army_1.units) - 1:

                legion_1 = army_1.units[unit_army1_nmb], \
                           army_1.units[unit_army1_nmb + 1]

            else:
                legion_1 = army_1.units[unit_army1_nmb], None

            if fight(legion_1[0], legion_2[0], legion_1[1], legion_2[1]):
                unit_army2_nmb += 1
            else:
                unit_army1_nmb += 1

        return army_1.units[-1].is_alive


def fight(unit_1, unit_2, unit_1_2=None, unit_2_2=None):
    """Init fight between two units while health one of them > 0

    :param unit_1: object of Warrior or Warrior sub classes
    :param unit_2: object of Warrior or Warrior sub classes
    :param unit_1_2: object of Warrior or Warrior sub classes
    :param unit_2_2: object of Warrior or Warrior sub classes
    :return: Unit_1.is_alive property
    """

    def defender_fight(unit_a, unit_b):
        """Init attack from unit_a to unit_b

        :param unit_a: object of Warrior or Warrior sub classes
        :param unit_b: object of Warrior or Warrior sub classes
        :return: unit_a attack level
        """
        if 'defense' in unit_b.__dict__:
            attack = unit_a.attack - unit_b.defense \
                if unit_a.attack > unit_b.defense else 0
        else:
            attack = unit_a.attack
        unit_b.health -= attack
        return attack

    def vampire_recovery(unit, attack):
        """Recovery health parameter if unit has attr 'vampirism'

        :param unit: object of Warrior or Warrior sub classes
        :return: None
        """
        if 'vampirism' in unit.__dict__:
            unit.health += attack * (unit.vampirism / 100)
        return

    def lancer_attack(unit, attack, second_unit):
        """Init attack to second unit in enemy army

        :param unit: object of Lancer class
        :param attack: half attack level of unit to first enemy unit
        :param second_unit: object of Warrior or Warrior sub classes
        :return: None
        """
        if second_unit:
            self_unit_attack, unit.attack = unit.attack, attack / 2
            defender_fight(unit, second_unit)
            unit.attack = self_unit_attack
        return

    while True:
        if unit_1.health > 0:
            attack = defender_fight(unit_1, unit_2)
            lancer_attack(unit_1, attack, unit_2_2)
            vampire_recovery(unit_1, attack)
        else:
            break
        if unit_2.health > 0:
            attack = defender_fight(unit_2, unit_1)
            lancer_attack(unit_2, attack, unit_1_2)
            vampire_recovery(unit_2, attack)
        else:
            break
    return unit_1.is_alive


if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army)
    assert not battle.fight(army_3, army_4)
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army)
    assert not battle.fight(army_3, army_4)
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive
    assert not fight(bob, mike)
    assert fight(lancelot, rog)

    # battle tests
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

    assert not battle.fight(my_army, enemy_army)
    assert battle.fight(army_3, army_4)
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive
    assert not fight(bob, mike)
    assert fight(lancelot, rog)
    assert not fight(eric, richard)
    assert fight(ogre, adam)

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert not battle.fight(my_army, enemy_army)
    assert battle.fight(army_3, army_4)
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce)
    assert not fight(dave, carl)
    assert chuck.is_alive
    assert not bruce.is_alive
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive
    assert not fight(bob, mike)
    assert fight(lancelot, rog)
    assert not fight(eric, richard)
    assert fight(ogre, adam)
    assert fight(freelancer, vampire)
    assert freelancer.is_alive

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army)
    assert not battle.fight(army_3, army_4)
    print("Coding complete? Let's try tests!")
