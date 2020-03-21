""" https://py.checkio.org/mission/digits-multiplication/solve/

You are given a positive integer. Your function should calculate the product
of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120
(don't forget to exclude zeroes).
Input: A positive integer.
Output: The product of the digits as an integer.
Precondition: 0 < number < 106
"""


def test_digits_multiplication():

    def checkio(number: int) -> int:
        if number:
            product = 1
        else:
            product = 0
        while number:
            digit = number % 10
            if digit:
                product *= digit
            number //= 10
        return product

    print('Digits multiplication result is:', checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1


if __name__ == '__main__':
    test_digits_multiplication()
