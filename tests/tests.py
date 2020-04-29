import ddt
import unittest
from task3 import pow_two


@ddt.ddt
class TestSimple(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            pow_two('1')

    def test_negative(self):
        self.assertFalse(pow_two(-1), True)
        self.assertFalse(pow_two(0), True)

    @ddt.data(
        (10, 8),
        (20, 16),
        (1, 1),
        (13, 16),
        (0, False),
    )
    @ddt.unpack
    def test_diff(self, num, expected):
        self.assertEqual(pow_two(num), expected)
