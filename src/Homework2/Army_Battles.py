"""Army Battles

In this mission your task is to add new classes and functions to the existing
ones. The new class should be the Army and have the method add_units() -
for adding the chosen amount of units to the army. The first unit added will
be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will
determine the strongest army. The battles occur according to the following
principles: at first, there is a duel between the first warrior of the first
army and the first warrior of the second army. As soon as one of them
dies - the next warrior from the army that lost the fighter enters the duel,
and the surviving warrior continues to fight with his current health. This
continues until all the soldiers of one of the armies die. In this case, the
battle() function should return True, if the first army won, or False, if
 the second one was stronger.

"""
# Taken from mission The Warriors
from collections import deque


class Warrior(object):
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self, attack=7):
        super(Knight, self).__init__()
        self.attack = attack


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        self.health = health
        self.attack = attack
        self.defense = defense


class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirizm=50):
        self.health = health
        self.attack = attack
        self.vampirism = vampirizm


class Lancer(Warrior):
    def __init__(self, health=50, attack=6):
        self.health = health
        self.attack = attack


def fight(unit_1, unit_2, arm_1=None, arm_2=None):
    def vampire_hilling(vamp, other):
        if hasattr(other, 'defense'):
            if other.defense < vamp.attack:
                hill = (vamp.attack - other.defense) * vamp.vampirism / 100
                vamp.health += hill
        else:
            vamp.health += vamp.attack * (vamp.vampirism / 100)

    def fight_step(attack_unit, def_unit):
        if hasattr(def_unit, 'defense'):
            if def_unit.defense < attack_unit.attack:
                def_unit.health -= (attack_unit.attack - def_unit.defense)
        else:
            def_unit.health -= attack_unit.attack

        if hasattr(attack_unit, 'vampirism'):
            vampire_hilling(attack_unit, def_unit)

    def lancer_hit_second_enemy(lancer, other_army):
        if len(other_army.queue) > 0:
            s_unit = other_army.queue[0]
            if hasattr(s_unit, 'defense'):
                if s_unit.defense < (lancer.attack * 0.5):
                    s_unit.health -= ((lancer.attack * 0.5) - s_unit.defense)
            else:
                s_unit.health -= lancer.attack * 0.5

    while unit_1.is_alive and unit_2.is_alive:
        fight_step(unit_1, unit_2)
        if isinstance(unit_1, Lancer) and arm_2 is not None:
            lancer_hit_second_enemy(unit_1, arm_2)
        if not unit_2.is_alive:
            break
        fight_step(unit_2, unit_1)
        if isinstance(unit_2, Lancer) and arm_1 is not None:
            lancer_hit_second_enemy(unit_2, arm_1)
        if not unit_1.is_alive:
            break
    return unit_1.health > unit_2.health


class Army(object):
    def __init__(self):
        self.queue = deque()

    def add_units(self, unit_class, count):
        for ind in range(count):
            self.queue.append(unit_class())


class Battle(object):
    def fight(self, army_1, army_2):
        if len(army_1.queue) > 0 and len(army_2.queue) == 0:
            return True
        elif len(army_1.queue) == 0 and len(army_2.queue) > 0:
            return False
        elif len(army_1.queue) == 0 and len(army_2.queue) == 0:
            return True
        else:
            unit_a1 = army_1.queue.popleft()
            unit_a2 = army_2.queue.popleft()
        while True:
            if fight(unit_a1, unit_a2):
                if len(army_2.queue) > 0:
                    unit_a2 = army_2.queue.popleft()
                else:
                    return True
            else:
                if len(army_1.queue) > 0:
                    unit_a1 = army_1.queue.popleft()
                else:
                    return False


if __name__ == '__main__':
    # These "asserts" using only for auto-testing

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

    print("Coding complete! First part of tests passed!!!")

if __name__ == '__main__':
    # These "asserts" using only for auto-testing

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
    print("Coding complete! Second part of tests passed!!!")

if __name__ == '__main__':
    # These "asserts" using only for auto-testing

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
    print("3 part tests passed!!!")

if __name__ == '__main__':
    # These "asserts" using only for auto-testing

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
    # These "asserts" using only for auto-testing

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
    print("All tests passed. Test Finish!!!")
