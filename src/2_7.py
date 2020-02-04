"""
- Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

import math

number = number_iter = int(input("Insert the number: "))

new_number = 0

# Len of the number
number_len = int(math.log10(number) + 1)

# print(number_len)

# Last number of the number_iter ->
# -> first number of the new_number
# Last number of the refreshed number_iter ->
# -> second number of the new_number
# ...
for number_len in range(number_len, 0, -1):
    #    print(number_iter)
    new_number = new_number * 10 + number_iter % 10
    number_iter = int(number_iter / 10)

# print(new_number)

print("The number is palindrome? -", number == new_number)
