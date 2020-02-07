"""Flatten a List.

There is a list which contains integers or other nested lists which may
contain yet more lists and integers which then… you get the idea. You
should put all of the integer values into one flat list. The order should
be as it was in the original list with string representation from left
to right.

flat_lst([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_lst([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

"""


def flat_list(array, rez=None):
    rez = rez or []
    for item in array:
        if not isinstance(item, list):
            rez.append(item)
        else:
            rez = flat_list(item, rez)
    return rez


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3]
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert flat_list([[[2]], [4, [5, 6, [6], 6], 7]]) == [2, 4, 5, 6, 6, 6, 7]
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
    print('Done! Check it')
