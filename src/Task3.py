"""Оформите указанную задачу из прошлых домашних в виде функции
и покройте тестами. Учтите, что в функцию могут быть переданы
некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные
ситуации сама"""


import unittest

import ddt

from src import the_maximum_divisor


@ddt.ddt
class TestSimple(unittest.TestCase):
    @ddt.data(
        (10, 2),
        (16, 16),
        (12, 4),
    )
    @ddt.unpack
    def test_different_cases(self, num, expected):
        """Test {}, the maximum divisor in power 2 is {}"""
        result = the_maximum_divisor.maximum_divisor(num)
        self.assertEqual(result, expected)

    def test_bad_nums(self):
        with self.assertRaises(TypeError):
            the_maximum_divisor.maximum_divisor("asd")
        with self.assertRaises(TypeError):
            the_maximum_divisor.maximum_divisor([1, 2, 3])
        with self.assertRaises(TypeError):
            the_maximum_divisor.maximum_divisor(1, 2)
