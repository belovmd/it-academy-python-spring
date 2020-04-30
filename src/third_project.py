"""Оформите указанную задачу из прошлых домашних в виде функции и

покройте тестами. Учтите, что в функцию могут быть переданы некорректные

значения, здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию

для того чтобы она ловила все возможные ситуации самаю

"""

from ddt import ddt
from ddt import data
from ddt import unpack
import unittest


def total_amount(rubles, kopecks, quantity):
    """Напишите программу, которая считает общую цену.

    водится M рублей и N копеек цена, а также количество L товара.

    Посчитайте общую цену в рублях и копейках за L товаров.

    """

    result_rubles = rubles * quantity + kopecks * quantity // 100
    result_kopecks = kopecks * quantity % 100
    return "{0} rubles {1} kopecks for {2} product".format(result_rubles,
                                                           result_kopecks,
                                                           quantity,
                                                           )


@ddt
class TestSimple(unittest.TestCase):
    def test_with_string(self):
        with self.assertRaises(TypeError):
            total_amount('50, 50, 50')

    def test_with_list(self):
        with self.assertRaises(TypeError):
            total_amount([5, 5, 5])

    @data(
        (total_amount(10, 33, 400), '4132 rubles 0 kopecks for 400 product'),
        (total_amount(50, 50, 50), '2525 rubles 0 kopecks for 50 product'),
        (total_amount(23, 36, 111), '2592 rubles 96 kopecks for 111 product'),
        (total_amount(535, 14, 543), '290581 rubles 2 kopecks for 543 product')
    )
    @unpack
    def test_main(self, introduced, expected):
        self.assertEqual(introduced, expected)


if __name__ == '__main__':
    unittest.main()
