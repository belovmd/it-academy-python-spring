""" Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""

first_number = second_number = 1
n = int(input("Введите n-ое число Фибоначчи: "))
while n > 2:
    first_number, second_number = second_number, first_number + second_number
    n -= 1
print(second_number)
