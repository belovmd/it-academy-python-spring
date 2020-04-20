"""Даны два натуральных числа. Вычислите их наибольший общий делитель

при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

"""

first_number = 30
second_number = 18
while first_number and second_number:
    first_number, second_number = second_number, first_number % second_number
print(first_number)
