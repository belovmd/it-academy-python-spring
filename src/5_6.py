"""Вводится число найти его
максимальный делитель, являющийся
степенью двойки. 10(2) 16(16), 12(4).
"""


import math

number = int(input("Insert the number: "))

max_divisor = 2 ** int(math.log2(number))
while (number % max_divisor) != 0:
    max_divisor >>= 1
print(max_divisor)
