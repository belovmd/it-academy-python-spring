from ddt import data
from ddt import ddt
from ddt import unpack
import unittest
from time import time


def timed(func):
    def wrapper(*args):
        start = time()
        result = func(*args)
        print("Executing %s took %d ms" % (func.__name__, (time() - start) * 1000))
        return result

    return wrapper


@timed
def euler268(nn):
    # Список простых числе до 100
    n = 100
    a = list(range(2, n + 1))

    for el in a:
        if el:
            for elem in range(2 * el, n + 1, el):
                a[elem - 2] = 0
    prime_numb_list = list(filter(lambda x: x != 0, a))


    # Перебор вариантов
    counter = 0

    for el in range(1, nn + 1):
        count = 0
        for number in range(0, len(prime_numb_list)):
            if el % prime_numb_list[number] == 0:
                count += 1
                if count == 4:
                    counter += 1

    return counter


if __name__ == '__main__':
    euler268(10 ** 6)


@ddt
class Euler268TestCase(unittest.TestCase):
    @data(
        (euler268(100), 0),
        (euler268(1000), 23),
        (euler268(10 ** 6), 77579),
    )
    @unpack
    def test_main(self, inpt, outpt):
        self.assertEqual(inpt, outpt)

    @data('1000', [1000, ], (1000, ), {1000, }, None)
    def test_wrong_inp(self, nn):
        with self.assertRaises(TypeError):
            euler268(nn)

    def test_empty(self):
        with self.assertRaises(TypeError):
            euler268()

    @data(1000, 1, 10, 1000)
    def test_negative_and_zero_numb(self, nn):
        self.assertGreater(nn, 0)


if __name__ == '__main__':
    unittest.main()
