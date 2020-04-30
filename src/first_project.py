"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,

покупка билета в транспортной компании, или простая РПГ. Создайте несколько

объектов классов, которые описывают ситуацию Объекты должны содержать как

атрибуты так и методы класса для симуляции различных действий.

Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -

вызывать методы, взаимодействие объектов и т.д.

"""

import random


class Person:
    def __init__(self, name, health, intoxication, satiety, mood):
        self.name = name
        self.health = health
        self.intoxication = intoxication
        self.satiety = satiety
        self.mood = mood


class Party(Person):
    def welcome(self):
        print('Добрый вечер, {}'.format(self.name))

    def food(self):
        if self.health >= 80:
            print('Ты не голоден')
        else:
            print('Вы хотите кушать!')
            print('Выбери еду:pizza, burger, sandwich')
            food = input('Введи выбор: ')
            if food == 'pizza':
                self.health += 30
                self.mood += 20
            elif food == 'burger':
                self.health += 15
                self.mood += 15
            elif food == 'sandwich':
                self.health += 10
                self.mood += 10
            else:
                print('Такой еды нет')

    def drink(self):
        if self.intoxication >= 100:
            print('Тебе пора домой')
        else:
            print('Надо выпить!')
            print('Выбери напиток:vodka, vine, beer')
            drink = input('Введи выбор: ')
            if drink == 'vodka':
                self.intoxication += 15
                self.health -= 10
                self.mood += 10
            elif drink == 'vine':
                self.intoxication += 10
                self.health -= 5
                self.mood += 10
            elif drink == 'beer':
                self.intoxication += 5
                self.health -= 5
                self.mood += 10
            else:
                print('такого напитка нет')

    def dance(self):
        if self.health <= 25 and self.mood <= 25:
            print('Ты устал для танцев')
        elif self.intoxication <= 0:
            self.health -= 10
            self.mood += 15
        else:
            self.intoxication -= 5
            self.health -= 10
            self.mood += 15

    def your_condition(self):
        print('После вечеринки вы пошли домой в состоянии: '
              'здоровье={}, опьянение={}, сытость={}, настроение={}'.format(
                self.health,
                self.intoxication,
                self.satiety,
                self.mood,)
              )


if __name__ == '__main__':
    person = Party('Andrei', 50, 0, 30, 15)
    person_method = [person.food, person.drink, person.dance]
    person.welcome()
    for _ in range(5):
        random_method = random.choice(person_method)
        random_method()
    person.your_condition()
