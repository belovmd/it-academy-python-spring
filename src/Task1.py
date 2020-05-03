"""Создайте  модель из жизни. Это может быть бронирование комнаты
в отеле, покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для
симуляции различных действий. Программа должна инстанцировать
объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""


class Warrior(object):
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def hero_status(self):
        if self.health > 0:
            print("{name}. Race: {race} ({level} lvl). HP: {health}%"
                  .format(name=self.name,
                          race=self.race,
                          level=self.level,
                          health=self.health))
        else:
            print("{name}: Race: {race} ({level} level). Dead"
                  .format(name=self.name,
                          race=self.race,
                          level=self.level))

    def farm(self):
        """Warrior start farming creeps"""
        if self.health:
            self.level += 1
            self.health -= 5

    def regeneration(self):
        if self.health:
            self.health = 100

    def fight(self, opponent):
        winner = ''
        while not winner:
            opponent.health -= self.level
            if not opponent.health > 0:
                winner = self.name
                break
            self.health -= opponent.level
            if not self.health > 0:
                winner = opponent.name
                break
        print("Duel winner: ", winner)


warrior1 = Warrior("Shadow Fiend", 1, "Demon")
warrior2 = Warrior("Lina", 1, "Humanoid")

warrior1.hero_status()
warrior2.hero_status()
for _ in range(10):
    warrior1.farm()
for _ in range(8):
    warrior2.farm()
warrior1.hero_status()
warrior2.hero_status()
warrior1.regeneration()
warrior2.regeneration()
warrior1.fight(warrior2)
warrior1.hero_status()
warrior2.hero_status()
