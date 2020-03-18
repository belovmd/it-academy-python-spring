""" Greatest common factor


There are two natural numbers. Using Euclid Algorithm calculate the greatest
common factor. Do not use functions and recursion.
"""

print('Input a, b:')
a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)
