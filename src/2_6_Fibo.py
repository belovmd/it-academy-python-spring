"""
- Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы.
n - вводится
"""

n = int(input("Insert the number: "))

fibo_n_minus_1 = 0
fibo_n = 1

"Initial state: Fn = 1, n == i = 1"
i = 1

while i < n:
    fibo_n += fibo_n_minus_1
    fibo_n_minus_1 = fibo_n - fibo_n_minus_1
    i += 1

"""
After 1st cycle:
Fn = 1, n == i = 2
After 2nd cycle:
Fn = 2, n == i = 3
After 3th cycle:
Fn = 3, n == i = 4
...
"""



print("Fibonacci number: ", fibo_n)
