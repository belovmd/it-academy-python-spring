""" 7. Оглянемся назад
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

number1 = int(input("Введите первое целое число: "))
number2 = int(input("Введите второе целое число: "))
while number2:
    number1, number2 = number2, number1 % number2
print("Наибольший общий делитель:", number1)