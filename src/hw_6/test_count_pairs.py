""" Tests writing

Variant 3: homework 3 task 4
"""

from itertools import combinations
from ddt import ddt, data, unpack

import unittest


def count_pairs(elements):
    all_combinations = list(combinations(elements, 2))
    equal_pairs = [el for el in all_combinations if el[0] == el[1]]
    return len(equal_pairs)


@ddt
class TestCountPairs(unittest.TestCase):

    @data([[1, 2, 3, 1, 2, 3], 3],
          [['qqq', 'w', 'ww', 'end', 'ww', 'qqq', 'end', 'w'], 4],
          [[1, '1', '3', 4, '4', 3], 0],
          [['word', '23', 23, 23, '23', 'word', '23'], 5],
          [[1, 1, 1], 3],
          [[2.3, 2.3, 2.3, 2.3], 6],
          [['', '', ''], 3],
          [[0, 0, 0, 0, 0], 10],
          [[-2, 4.5, -2, 55, 'qew', -2], 3],
          [[3, 3, 3, 3, 3, 3, 3, 3, 3], 36],
          ['eeeewe', 10],
          [('a', 'a', 's', 's', 'a', 'a'), 7],)
    @unpack
    def test_pairs_logic(self, elements, expected):
        actual = count_pairs(elements)
        self.assertEqual(expected, actual)

    def test_set(self):
        elements = set([123, 234, 345, 123])
        expected = 0
        actual = count_pairs(elements)
        self.assertEqual(expected, actual)

    def test_func_as_an_argument(self):
        def foo():
            pass
        with self.assertRaises(TypeError):
            count_pairs(foo)

    @data(4, 5.5, True)
    def test_non_iterable(self, elements):
        with self.assertRaises(TypeError):
            count_pairs(elements)


if __name__ == '__main__':
    unittest.main()
