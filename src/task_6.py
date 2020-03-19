def pow_binary(number):
    """Power of two

    :param number: integer number
    :return: nearest to number power of two
    """
    tmp_pow = 1
    while number > tmp_pow << 1:
        tmp_pow <<= 1
    return min(tmp_pow, tmp_pow << 1, key=lambda x: abs(x - number))


if __name__ == '__main__':
    for i in range(-8, 34):
        print('Nearest power of two to {} is {}'.format(i, pow_binary(i)))

    i = 1000000000000000000000000000000000000000000000000000000000000000000000
    print('Nearest power of two to {} is {}'.format(i, pow_binary(i)))
