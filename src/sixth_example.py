# Выведите n-ое число Фибоначчи,
# используя только временные переменные,
# циклические операторы и условные операторы.
# n - вводится

quantity = int(input("Enter number Fibonacci: "))
first__elem = 1
second_elem = 1
if first__elem == 1:
    print(1)
if second_elem == 1:
    print(1)
for i in range(quantity):
    first__elem, second_elem = second_elem, first__elem + second_elem
    print(second_elem)
