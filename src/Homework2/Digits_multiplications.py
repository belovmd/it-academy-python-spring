"""Digits_multiplications.

You are given a positive integer. Your function should calculate the product
of the digits excluding any zeroes. For example: The number given is 123405.
The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

"""
from functools import reduce


def milt_digits(number: int) -> int:
    digits = [d for d in str(number) if d != '0']
    return reduce((lambda a, b: a * b), list(map(int, digits)))


if __name__ == '__main__':
    assert milt_digits(123405) == 120
    assert milt_digits(999) == 729
    assert milt_digits(1000) == 1
    assert milt_digits(1111) == 1
    print('Done!')
