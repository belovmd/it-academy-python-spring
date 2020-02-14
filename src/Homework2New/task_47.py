def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """Format a number as friendly text, using common suffixes.

    Input: A number as an integer.
    The keyword argument "base" as an integer, default 1000.
    The keyword argument "decimals" as an integer, default 0.
    The keyword argument "powers" as a list of string,
    default ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']

    Output: The converted number as a string
    """

    res_number = abs_nmb = abs(number)
    res_pow = 0

    while res_number >= base:
        res_number //= base
        res_pow += 1

    if res_pow > len(powers) - 1:
        res_pow = -1
        res_number = abs_nmb // (base ** (len(powers) - 1))

    res_number = res_number * (1 - 2 * (number < 0))
    res_dec = abs_nmb / (base ** res_pow) - abs_nmb // (base ** res_pow)
    res_dec = f'{res_dec:.{decimals}f}'[1:]

    return f'{res_number}{res_dec}{powers[res_pow]}{suffix}'


if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000,
                           base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=["", "d", "D"]) == "-1d"
    assert friendly_number(-155, base=100, decimals=1,
                           powers=["", "d", "D"]) == "-1.6d"
    assert friendly_number(255000000000, powers=["", "k", "M"]) == '255000M'
