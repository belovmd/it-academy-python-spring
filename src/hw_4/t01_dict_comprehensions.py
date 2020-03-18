""" Dict comprehensions

Use dict-comprehensions to create a dictionary:
keys: numbers from 1 to 20
values: key**3
"""


dct = {key: key**3 for key in range(1, 21)}
print(dct)
