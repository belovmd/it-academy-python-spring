"""Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)

"""

number = first_number = int(input("Введите число: "))
second_number = 0
while first_number > 0:
    second_number *= 10
    second_number += first_number % 10
    first_number //= 10
if second_number == number:
    print("Число %s полиндорм!" % number)
else:
    print("Число %s не полиндорм!" % number)
