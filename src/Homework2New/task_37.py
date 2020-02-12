class Warrior:
    """ Warrior class

    Two parameters in class constructor: health and attack
    One property is_alive if health parameter > 0
    """

    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    """Sub class of Warrior class with own parameter values in constructor"""

    def __init__(self, health=50, attack=7):
        Warrior.__init__(self, health, attack)


def fight(unit_1, unit_2):
    """Init fight between two units while health of them > 0

    :param unit_1: object of Warrior or Knight class
    :param unit_2: object of Warrior or Knight class
    :return: Unit_1.is_alive property
    """
    while True:
        if unit_1.health > 0:
            unit_2.health -= unit_1.attack
        else:
            break
        if unit_2.health > 0:
            unit_1.health -= unit_2.attack
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
