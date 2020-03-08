"""
- Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы.
n - вводится
"""


n = int(input("Insert the number: "))

fibo_n_minus_1 = 0
fibo_n = 1

i = 1

while i < n:
    fibo_n += fibo_n_minus_1
    fibo_n_minus_1 = fibo_n - fibo_n_minus_1
    i += 1

print("Fibonacci number: ", fibo_n)
