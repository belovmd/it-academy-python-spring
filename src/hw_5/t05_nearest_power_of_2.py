""" The nearest power of two

Write a function that finds the nearest power of 2 to a number.
Example:
    10(8), 20(16), 1(1), 13(16).
"""


def get_the_nearest_power_of_2(n):
    m = 1
    while 1 << m <= n:
        m += 1
    less_pow = 1 << m - 1
    more_pow = 1 << m
    return less_pow if n - less_pow < more_pow - n else more_pow


if __name__ == '__main__':
    assert get_the_nearest_power_of_2(10) == 8, 'Test 1'
    assert get_the_nearest_power_of_2(20) == 16, 'Test 2'
    assert get_the_nearest_power_of_2(1) == 1, 'Test 3'
    assert get_the_nearest_power_of_2(13) == 16, 'Test 4'

    number = 10633823966279326983230456482242756609
    expected_2_pow_123 = 10633823966279326983230456482242756608
    assert get_the_nearest_power_of_2(number) == expected_2_pow_123, 'Test 5'
