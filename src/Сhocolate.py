""" Шоколадка **
Определения:
Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
Разлом - деление шоколадки на две части с натуральными размерами по прямой.
Долька - элемент шоколадки размером 1х1. Очевидно шоколадка состоит из n*m долек.
Кусок - элемент шоколадки произвольного (целочисленного размера).

Определите, можно ли одним разломом отделить от шоколадки кусок площадью ровно k.
Определите, можно ли отломить от шоколадки ровно k долек за некоторое количество разломов.
Определите, можно ли отломить от шоколадки ровно k долек с помощью t разломов
Описание решения поместите в docstring
"""

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
t = int(input("Введите t: "))

"""Можно ли одним разломом отделить от шоколадки кусок площадью ровно k.

Если количество желаемых кусков меньше чем кол-во кусков в шоколадке
то ее можно поделить. Если количество кусочков в одной из сторон
делится без остатка, то ее можно поделить за 1 разлом
"""
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Одним разломом можно получить кусок площадью ", k)
else:
    print("Одним разломом нельзя получить кусок площадью ", k)

"""Можно ли отломить от шоколадки ровно k долек за некоторое количество разломов.

Если шоколадка больше чем нам нужно, нам придется ее поделить
минимум 1 раз. Поскольку нельзя что бы остался 1 кусок, их должно
остаться минимум 2.
Следовательно 1 <= желаемое количество <= (n * m) - 2
"""
if 1 <= k <= (n * m) - 2:
    print("За некоторое количество разломов можно отломать {} кусков.".format(k))
else:
    print("За некоторое количество разломов нельзя отломать {} кусков.".format(k))

"""Можно ли отломить от шоколадки ровно k долек с помощью t разломов

Если k / 2 ** 7 <= 1 то можно получить k долек за t разломов.
Количество оставшихся кусков после деления шоколадки должно быть не менее 2
"""
if k+2 <= n * m:

    if k / 2 ** 7 <= 1:
        print("За {} разломов можно получить {} кусков".format(t, k))
    else:
        print("За {} разломов нельзя получить {} кусков".format(t, k))
