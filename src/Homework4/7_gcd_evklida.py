"""Задача 7

Даны два натуральных числа. Вычислите их наибольший общий делитель при
помощи алгоритма Евклида (мы не знаем функции и рекурсию).

"""
first = int(input('Enter number 1:'))
second = int(input('Enter number 2:'))
while first != second:
    if first > second:
        first, second = first - second, second
    else:
        first, second = second - first, first
print(f'GCD = {first}')
