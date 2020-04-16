import os
import unittest

from .t03_biggest_number import biggest_number
from ddt import data
from ddt import ddt
from ddt import unpack


@ddt
class TestBiggestNumber(unittest.TestCase):

    @data([['23', '45'], '4523', 'Simple test'],
          [['0', '30', '200', '101'], '302001010', 'Test with zero'],
          [[], '', 'Test empty input'],
          [['94', '83', '9', '991', '11', '342', '35', '34274'],
           '99919483353427434211', 'Test numbers with different length'],
          [['22', '2222', '22', '222', '22'], '2222222222222',
           'Test the same numbers'],)
    @unpack
    def test_sorting_logic(self, numbers, expected, message):
        """Test sorting logic"""

        actual = biggest_number(numbers)
        self.assertEqual(expected, actual, msg=message)

    def test_bad_input(self):
        """Test that exception raises when using list of int as input"""

        numbers = [1, 3, 9, 34]
        with self.assertRaises(TypeError):
            biggest_number(numbers)

    def test_bigger_input(self):
        """Test bigger and correct input"""

        numbers = []
        dir_name = os.path.dirname(__file__)
        input_file_path = dir_name + '/files/t03_input.txt'
        with open(input_file_path, 'r') as file:
            for line in file:
                numbers.extend(line.strip().split())
        result = biggest_number(numbers)

        expected_file_path = dir_name + '/files/t03_expected.txt'
        expected = ''
        with open(expected_file_path, 'r') as file:
            for line in file:
                expected += line.strip()

        self.assertEqual(expected, result)

    def test_none_input(self):
        """Test that exception raises when input parameter is None"""

        with self.assertRaises(TypeError):
            biggest_number(None)
