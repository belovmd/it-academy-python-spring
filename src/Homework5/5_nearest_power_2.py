"""5 - nearest power of two

Написать программу которая находит ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1), 13(16)
"""


def nearest_power_of_2(number):
    power = 0
    while True:
        result = 1 << power
        if result > number:
            break
        power += 1
    diff_up = abs(result - number)
    diff_down = abs((1 << power - 1) - number)
    return 2**power if diff_up <= diff_down else 2**(power - 1)


if __name__ == '__main__':
    assert nearest_power_of_2(10) == 8
    assert nearest_power_of_2(20) == 16
    assert nearest_power_of_2(13) == 16
