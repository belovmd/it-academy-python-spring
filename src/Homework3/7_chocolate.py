"""Шоколадка **

Определения:
Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
Разлом - деление шоколадки на две части с натуральными размерами по прямой.
Долька - элемент шоколадки размером 1х1. Очевидно шоколадка состоит из n*m
долек.
Кусок - элемент шоколадки произвольного (целочисленного размера).

1)Определите, можно ли одним разломом отделить от шоколадки кусок площадью
ровно k.
2)Определите, можно ли отломить от шоколадки ровно k долек за некоторое
количество разломов.
3)Определите, можно ли отломить от шоколадки ровно k долек с помощью t разломов

"""


def chocolate_1(choco_array, k):
    """Solve 1 task.

    First step - define count rows and cols of chocolate
    Second step - break chocolate along rows and calculate count pieces
    size 1x1. Then break chocolate along cols and calculate count pieces too.
    All calculated results put into list pieces_in_slice.
    In the finally step we are checking do contain k in list pieces_in_slice.

    """
    col, row = len(choco_array), len(choco_array[0])
    pieces_in_slice = list()
    for ind in range(1, row):
        pieces_in_slice.append(ind * col)
    for ind in range(1, col):
        pieces_in_slice.append(ind * row)
    if k in pieces_in_slice:
        return True
    return False


if __name__ == '__main__':
    assert chocolate_1([[1, 1, 1], [1, 1, 1]], 2)
    assert not chocolate_1([
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]], 5)
    assert chocolate_1([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]], 15)
