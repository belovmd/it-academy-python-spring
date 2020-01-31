# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

quantity = int(input("Enter number Fibonacci: "))
first__fibonacci = 1
second_fibonacci = 1
if first__fibonacci == 1:
    print(1)
if second_fibonacci == 1:
    print(1)
for i in range(quantity):
    fibonacci = first__fibonacci + second_fibonacci
    first__fibonacci = second_fibonacci
    second_fibonacci = fibonacci
    print(fibonacci)