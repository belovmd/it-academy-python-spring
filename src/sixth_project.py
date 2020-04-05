"""Вводится число найти его максимальный делитель,

являющийся степенью двойки. 10(2) 16(16), 12(4).

"""


def max_div(number):
    exponentiation = 1
    while number >> exponentiation > 0:
        div = 1 << exponentiation
        if number % div == 0:
            max_exponentiation = 1 << exponentiation
        exponentiation += 1
    return max_exponentiation


print(max_div(10))
print(max_div(16))
print(max_div(12))
