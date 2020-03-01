# 5) You are given an array of integers. You should find the sum of the
# integers with even indexes (0th, 2nd, 4th...). Then multiply this summed
# number and the final element of the array together. Don't forget that the
# first element has an index of 0.
# For an empty array, the result will always be 0 (zero).
# Input: A list of integers.
# Output: The number as an integer.


def checkio(array):
    s = 0
    if len(array) == 0:
        return 0
    else:
        for i in range(0, len(array), 2):
            s += array[i]
        return (array[len(array) - 1]) * s


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print(
        "Coding complete? Click 'Check' to review your tests and earn"
        "cool rewards!")
