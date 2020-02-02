import unittest


def count_digits(number):
    """Calculating count of digits in number.

    :param number: int
    :return: count of digits in number -> int

    """
    count_digits = 0
    while number > 0:
        number //= 10
        count_digits += 1
    return count_digits


def is_palindrome(n):
    """The function checks if the number is a palindrome.

    :param n: number
    :return: True if number is palindrome else False

    """
    while n > 10:
        end_digit = n % 10
        first_digit = n // (10 ** (count_digits(n) - 1))
        if end_digit != first_digit:
            return False
        n = (n - (first_digit * 10 ** (count_digits(n) - 1) + end_digit)) / 10
    else:
        return True


class TestIsPalindrom(unittest.TestCase):
    def test_is_palindrom(self):
        self.assertEqual(is_palindrome(121), True)
        self.assertEqual(is_palindrome(12321), True)
        self.assertEqual(is_palindrome(123444321), True)
        self.assertEqual(is_palindrome(1232112), False)


if __name__ == "__main__":
    unittest.main()
