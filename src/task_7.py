def nd_pow_of_two(number):
    """Largest divisor of number

    :param number: integer number != 0
    :return: largest divisor of number which also is a power of two
    """
    nd_pow = 1
    while number % nd_pow == 0:
        nd_pow <<= 1
    return nd_pow >> 1


if __name__ == '__main__':
    for i in range(1, 22):
        print('{}: {}'.format(i, nd_pow_of_two(i)))

    i = 1000000000000000000000000000000000000000000000000000000000000000000000
    print('{}: {}'.format(i, nd_pow_of_two(i)))
