"""Greatest common factor

a: integer
b: integer
greatest common factor of a and b
"""

a, b = int(input('a = ')), int(input('b = '))
a, b = max(a, b), min(a, b)
while a % b != 0:
    a, b = b, a % b
print(b)
