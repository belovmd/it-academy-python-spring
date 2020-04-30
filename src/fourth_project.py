"""Проект Эйлера. https://euler.jakumo.org/problems/pg/1.html. Задача 451.

Обобщите указанную задачу на свое усмотрение, решите ее, покройте тестами.

"""

from ddt import ddt
from ddt import data
from ddt import unpack
import unittest


def modular_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


@ddt
class TestSimple(unittest.TestCase):
    def test_with_string(self):
        with self.assertRaises(TypeError):
            modular_inverse('3, 7')

    def test_empty_value(self):
        with self.assertRaises(TypeError):
            modular_inverse()

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            modular_inverse(3, 7, 15)

    @data(
        (modular_inverse(2, 8), 1),
        (modular_inverse(3, 7), 5),
        (modular_inverse(2, 6), 1),
        (modular_inverse(5, 14), 3),

    )
    @unpack
    def test_main(self, introduced, expected):
        self.assertEqual(introduced, expected)


if __name__ == '__main__':
    unittest.main()
