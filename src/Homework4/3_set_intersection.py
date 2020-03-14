"""Задача 3

Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.

"""


def count_elements(lst, other):
    """Return count elements that contain at the same time in both lists"""
    return len(set(lst).intersection(set(other)))


if __name__ == '__main__':
    lst_1 = [2, 3, 4, 5, 6]
    lst_2 = [2, 6, 7, 4, 2]
    assert count_elements(lst_1, lst_2) == 3
