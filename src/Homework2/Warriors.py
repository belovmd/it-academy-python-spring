"""The Warriors.

Let's start with the simple task - one-on-one duel. You need to create the
class Warrior, the instances of which will have 2 parameters - health (equal
to 50 points) and attack (equal to 5 points), and 1 property - is_alive,
which can be True (if warrior's health is > 0) or False (in the other case).
In addition you have to create the second unit type - Knight, which should
be the subclass of the Warrior but have the increased attack - 7. Also you
have to create a function fight(), which will initiate the duel between 2
warriors and define the strongest of them. The duel occurs according to the
following principle: Every turn, the first warrior will hit the second and
this second will lose his health in the same value as the attack of the first
warrior. After that, if he is still alive, the second warrior will do the
same to the first one. The fight ends with the death of one of them. If
the first warrior is still alive (and thus the other one is not anymore),
the function should return True, False otherwise.

Round:   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
Warrior: 50 50 43 43 36 36 29 29 22 22 15 15 8  8  1  1  -6
Knight:  50 45 45 40 40 35 35 30 30 25 25 20 20 15 15 10 10 ==> Win

"""
import unittest


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


class TestFightWarriors(unittest.TestCase):
    def test_winner(self):
        chuck = Warrior()
        bruce = Warrior()
        carl = Knight()
        dave = Warrior()
        mark = Warrior()
        self.assertEqual(fight(chuck, bruce), True)
        self.assertEqual(fight(dave, carl), False)
        self.assertEqual(chuck.is_alive, True)
        self.assertEqual(bruce.is_alive, False)
        self.assertEqual(dave.is_alive, False)
        self.assertEqual(fight(carl, mark), False)
        self.assertEqual(carl.is_alive, False)


if __name__ == '__main__':
    unittest.main()
