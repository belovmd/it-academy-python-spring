"""Task: find all squares in rectangle.

The drawing below gives an idea of how to cut a given "true" rectangle into
squares ("true" rectangle meaning that the two dimensions are different).

Example tests:
test.assert_equals(sqInRect(5, 5), None)
test.assert_equals(sqInRect(5, 3), [3, 2, 1, 1])

"""
import unittest


def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    squares = list()
    while lng - wdth != 0:
        max_side, min_side = (lng, wdth) if lng > wdth else (wdth, lng)
        all_square = max_side * min_side
        part = all_square - min_side ** 2
        squares.append(int(min_side))
        lng = part / min_side
        wdth = min_side
    else:
        squares.append(int(lng))
    return squares


class TestSquaresInRectangle(unittest.TestCase):
    def test_define_squares(self):
        self.assertEqual(sq_in_rect(5, 3), [3, 2, 1, 1])
        self.assertEqual(sq_in_rect(4, 3), [3, 1, 1, 1])
        self.assertEqual(sq_in_rect(6, 2), [2, 2, 2])
        self.assertEqual(sq_in_rect(4, 4), None)


if __name__ == "__main__":
    unittest.main()
