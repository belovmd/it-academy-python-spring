"""Greatest common factor

a: integer
b: integer
greatest common factor of a and b
"""
a, b = int(input('a = ')), int(input('b = '))
while b != 0:
    a, b = b, a % b
print(a)
