"""Matrix Determinant.

Write a function that accepts a square matrix (N x N 2D array) and returns
 the determinant of the matrix. How to take the determinant of a matrix --
 it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.
A 2x2 matrix [ [a, b], [c, d] ] or
|a  b|
|c  d|

has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem
 to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|
|d e f|
|g h i|

the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
where det(a_minor) refers to taking the determinant of the 2x2 matrix created
by crossing out the row and column in which the element a occurs:
|- - -|
|- e f|
|- h i|

Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a
4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) +
c * det(c_minor) - d * det(d_minor)

"""
import unittest


def make_minor_matrix(matrix, ignore_ind):
    minor_matrix = []
    for v in matrix[1:]:
        if ignore_ind == 0:
            minor_matrix.append(v[1:])
        elif ignore_ind == len(matrix[0]) - 1:
            minor_matrix.append(v[:-1])
        else:
            minor_matrix.append(v[:ignore_ind] + v[ignore_ind + 1:])
    return minor_matrix


def determinant(L, total_determinant=0):
    if len(L) == 1:
        return L[0]

    if len(L) == 2:
        return L[0][0] * L[1][1] - L[0][1] * L[1][0]

    for ind, val in enumerate(L[0]):
        if ind == 0 or ind % 2 == 0:
            total_determinant += val * (determinant(make_minor_matrix(L, ind)))
        else:
            total_determinant -= val * (determinant(make_minor_matrix(L, ind)))
    return total_determinant


test_matrix = [
    [
        [1, 2, 3, 4],
        [5, 0, 2, 8],
        [3, 5, 6, 7],
        [2, 5, 3, 1],
    ],
    [
        [2, 5, 3, 6, 3],
        [17, 5, 7, 4, 2],
        [7, 8, 5, 3, 2],
        [9, 4, -6, 8, 3],
        [2, -5, 7, 4, 2],
    ],
    [
        [1, 2, 4, 0, 9],
        [2, 3, 4, 1, 1],
        [6, 7, 3, 9, 3],
        [2, 0, 3, 0, 2],
        [4, 5, 2, 3, 1],
    ],
]
test_result = [24, 2060, 1328, 88]


class TestMatrixDeterminant(unittest.TestCase):
    def test_define_determinant(self):
        for ind, matrix in enumerate(test_matrix):
            self.assertEqual(determinant(matrix), test_result[ind])


if __name__ == '__main__':
    unittest.main()
