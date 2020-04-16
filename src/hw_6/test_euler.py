""" Задача 455 - Последние цифры степеней

Пусть f(n) будет наибольшим положительным целым числом x меньше 10**9, таким
что последние 9 цифр n**x образуют число x (включая ведущие нули), или будет
равно нулю, если такое целое число не существует.

Например:
f(4) = 411728896 (4411728896 = ...490411728896)
f(10) = 0
f(157) = 743757 (157743757 = ...567000743757)
Σf(n), 2 ≤ n ≤ 103 = 442530011399
Найдите Σf(n), 2 ≤ n ≤ 106.

Обобщение: ищем в пределах до 10**3, берем во внимание последние 3 цифры.
Ищем сумму Σf(n), 2 ≤ n ≤ 10**3, решаем перебором.
"""


from ddt import data
from ddt import ddt
from ddt import unpack
import unittest


LAST_NUMBERS = 3
MAX = 1000
N = 2


def func(n):
    res = 0
    for x in range(1, 10 ** LAST_NUMBERS):
        if x == n**x % 10**LAST_NUMBERS:
            res = x
            break
    return res


def solve_euler_task(n_max):
    if n_max < N or n_max > MAX:
        print('N is out of range, n should be: {} <= n <= {}'.format(N, MAX))
    else:
        return sum(func(number) for number in range(2, n_max + 1))


@ddt
class TestEuler(unittest.TestCase):
    @data((8, 856),
          (2, 736),
          (10, 0),
          (13, 53),
          (17, 777),
          (190, 0),
          (191, 791),
          (999, 999),)
    @unpack
    def test_func(self, n, expected):
        """Test function func with correct input"""

        self.assertEqual(expected, func(n))

    @data((3, 736 + 387, 'Test for 3'),
          (10, 4288, 'Test for 10**1'),
          (1000, 448399, 'Test for higher bound'),
          (154, 66040, 'Test for summing logic'))
    @unpack
    def test_logic(self, n_max, expected, message):
        """Test logic to find sum(f(n)), 2 <= n <= n_max"""

        self.assertEqual(expected, solve_euler_task(n_max), msg=message)

    def test_logic_for_lower_bound(self):
        """Test for the lower bound"""

        n = 2
        expected = func(n)
        actual = solve_euler_task(n)
        self.assertEqual(expected, actual)

    @data(1, 1001, 10000, -3, 0, 1345)
    def test_out_of_range(self, n_max):
        """Test with out of range input"""

        self.assertIsNone(solve_euler_task(n_max))

    def test_that_returns_value(self):
        """Test that returns a value at least"""

        self.assertIsNotNone(solve_euler_task(11))

    @data('10', 'ten', 10.33, None)
    def test_incorrect_input(self, n):
        """Test that exception raises when input is incorrect"""

        with self.assertRaises(TypeError):
            solve_euler_task(n)
