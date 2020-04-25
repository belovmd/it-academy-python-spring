"""3 - tests for previous HW3 - task 5 (Variant 13: homework 3 task 5)
Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
того, чтобы она ловила все возможные ситуации сама.

Variant 13: homework 3 task 5
5) Уникальные элементы в списке.
Дан список. Выведите те его элементы, которые встречаются в списке только
один раз. Элементы нужно выводить в том порядке, в котором они встречаются
в списке.

"""
import unittest
import ddt


def unique_elements(lst):
    """Return unique elements in list"""
    unique_el, not_unique = set(lst), set()
    for element in lst:
        try:
            unique_el.remove(element)
        except KeyError:
            not_unique.add(element)
    unique = set(lst) - not_unique
    return [el for el in lst if el in unique]


@ddt.ddt
class TestUniqueElements(unittest.TestCase):
    @ddt.data(
        ([1, 2, 3, 1, 3, 5, 3], [2, 5]),
        ([3, 4, 2, 3, 1], [4, 2, 1]),
        (['r', 't', 'r', (1,)], ['t', (1,)]),
        ([('a', 'b'), ('a', 'c'), ('a', 'b')], [('a', 'c')]),
        ([2, 2, 2, 2, 2, 2, 2], [])
    )
    @ddt.unpack
    def test_with_hashible_elements_in_list(self, inp_data, expected):
        self.assertEqual(unique_elements(inp_data), expected)

    def test_with_empty_list(self):
        self.assertEqual([], [])

    def test_with_unhashible_elements_in_list(self):
        with self.assertRaises(TypeError):
            unique_elements([{1, 2}, {'2': 2}])

    def test_with_not_iterable_object(self):
        with self.assertRaises(TypeError):
            unique_elements(1)


if __name__ == '__main__':
    unittest.main()
