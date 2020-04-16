"""Оглянемся назад
Даны два натуральных числа. Вычислите
их наибольший общий делитель при
помощи алгоритма Евклида (мы не знаем
функции и рекурсию).
"""


a = int(input("Insert first natural number: "))
b = int(input("Insert second natural number: "))

while a != 0 and b != 0:
    if a >= b:
        a %= b
    elif a < b:
        b %= a
    print(a or b)
