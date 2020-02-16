"""Skew-symmetric Matrix

In mathematics, particularly in linear algebra, a skew-symmetric matrix
(also known as an antisymmetric or antimetric) is a square matrix A which
is transposed and negative. This means that it satisfies the equation
A = −AT. If the entry in the i-th row and j-th column is aij, i.e.
A = (aij) then the symmetric condition becomes aij = −aji. You should
determine whether the specified square matrix is skew-symmetric or not.
You can find more details on Skew-symmetric matrices on its Wikipedia page.

Input: A square matrix as a list of lists with integers.
Output: If the matrix is skew-symmetric or not as a boolean.

Example:

is_symmetric_matrix([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) == True
is_symmetric_matrix([
    [ 0,  1, 2],
    [-1,  1, 1],
    [-2, -1, 0]]) == False
is_symmetric_matrix([
    [ 0,  1, 2],
    [-1,  0, 1],
    [-3, -1, 0]]) == False

"""


def is_symmetric_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != -matrix[col][row]:
                return False
    return True


if __name__ == '__main__':
    assert is_symmetric_matrix([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]])
    assert not is_symmetric_matrix([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]])
    assert not is_symmetric_matrix([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]])
    print("All tests passed")
