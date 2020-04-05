"""Написать программу которая находит ближайшую

степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)

"""


def pow_two(number):
    exponentiation = 1
    while 1 << exponentiation <= number:
        exponentiation += 1
    high = 1 << exponentiation - 1
    low = 1 << exponentiation
    if number - high < low - number:
        return high
    else:
        return low


print(pow_two(10))
print(pow_two(20))
print(pow_two(1))
print(pow_two(13))
