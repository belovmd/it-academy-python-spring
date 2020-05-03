def maximum_divisor(number):
    """Поиск максимального делителя,являющегося степенью двойки.

    Пример: 10(2) 16(16), 12(4)."""
    i = 1
    while number % i == 0:
        i <<= 1
    print("For the number {} the maximum divisor in power 2 is {}"
          .format(number, i >> 1))
    return i >> 1
