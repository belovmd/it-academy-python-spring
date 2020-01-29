"""
Calculate n-th Fibonacci number.
"""

print("Input n:")
n = int(input())

first = 1
second = 1
if n >= 1:
    print(first)
if n >= 2:
    print(second)
if n >= 3:
    i = 2
    while i < n:
        current = first + second
        print(current)
        first, second = second, current
        i += 1