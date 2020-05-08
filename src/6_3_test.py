from .t6_3 import get_ranges
from ddt import data
from ddt import ddt
from ddt import unpack
import unittest


@ddt
class GetRangesTestCase(unittest.TestCase):
    @data(
        (get_ranges([0, 1, 2, 3, 4, 7, 8, 10]), "0-4, 7-8, 10"),
        (get_ranges([4, 7, 10]), "4, 7, 10"),
        (get_ranges([2, 3, 8, 9]), "2-3, 8-9"),
    )
    @unpack
    def test_main(self, inpt, outpt):
        self.assertEqual(inpt, outpt)

    def test_string(self):
        with self.assertRaises(TypeError):
            get_ranges('1, 2, 3')

    def test_int(self):
        with self.assertRaises(TypeError):
            get_ranges(1)

    def test_set(self):
        with self.assertRaises(TypeError):
            get_ranges({1, 2, 3})

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_ranges([])


if __name__ == '__main__':
    unittest.main()
