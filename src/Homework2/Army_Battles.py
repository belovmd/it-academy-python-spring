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
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            break
        unit_1.health -= unit_2.attack
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
    print("First part tests complete!!!")

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
    print('All tests complete')
