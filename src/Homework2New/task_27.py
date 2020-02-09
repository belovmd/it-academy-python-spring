"""Instructions

Flatten a List.
There is a list which contains integers or other nested lists which may
contain yet more lists and integers which then… you get the idea. You
should put all of the integer values into one flat list. The order should
be as it was in the original list with string representation from left
to right.

flat_lst([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_lst([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
"""


def flat_list(array):
    """Recursion method"""
    result = []
    if type(array) != list:
        return [array]
    for element in array:
        number = flat_list(element)
        if number:
            result += number
    return result


def flat_list2(array):
    """Convert to string method"""
    return [int(element.strip('[], ')) for element in str(array).split(',')
            if element.strip('[], ')]


if __name__ == '__main__':
    print(flat_list([1, 2, 3]))
    print(flat_list2([1, 2, 3]))
    print(flat_list([1, [2, 2, 2], 4]))
    print(flat_list2([1, [2, 2, 2], 4]))
    print(flat_list([[[2]], [[[[7]]]], [4, [5, [6, [6], 6, 6]], [9], 7]]))
    print(flat_list2([[[2]], [[[[7]]]], [4, [5, [6, [6], 6, 6]], [9], 7]]))
    print(flat_list([-1, [1, [-2], 1], -1]))
    print(flat_list2([-1, [1, [-2], 1], -1]))
    print('Done! Check it')
