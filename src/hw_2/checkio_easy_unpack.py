"""https://py.checkio.org/mission/easy-unpack/solve/

Your mission here is to create a function that gets a tuple and returns
a tuple with 3 elements - the first, third and second to the last
for the given array.

Input: A tuple, at least 3 elements long.
Output: A tuple.
"""


def easy_unpack(elements: tuple) -> tuple:
    first = elements[0]
    second = elements[2]
    third = elements[-2]
    return first, second, third


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
