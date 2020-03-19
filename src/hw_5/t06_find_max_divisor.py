""" Find max divisor

Find a maximum divisor d of a number n, d = 2**k.
Example:
    10(2) 16(16), 12(4).
"""


def get_max_divisor(n):
    return n ^ (n & (n - 1))


if __name__ == '__main__':
    assert get_max_divisor(10) == 2, 'Test 1'
    assert get_max_divisor(16) == 16, 'Test 2'
    assert get_max_divisor(12) == 4, 'Test 3'
