"""6 - find max divider is power of two

Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def max_divider(number):
    power_of_two = 0
    result = 1
    while True:
        divider = 1 << power_of_two
        if (number / divider) < 1:
            break
        else:
            if number % divider == 0:
                result = divider
        power_of_two += 1
    return result


if __name__ == "__main__":
    assert max_divider(10) == 2
    assert max_divider(16) == 16
    assert max_divider(12) == 4
    assert max_divider(15) == 1
