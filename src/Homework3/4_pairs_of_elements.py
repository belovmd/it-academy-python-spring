"""Pairs of elements.

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

"""


def count_pairs(num_string):
    """Return dict contains element: count of element's pairs"""
    count_el = dict()
    count_pairs_el = dict()
    for element in num_string.split():
        count_el[element] = count_el.get(element, 0) + 1
        count_pairs_el[element] += count_el[element] - 1
    return count_pairs_el


if __name__ == '__main__':
    assert count_pairs('1 1 1 1') == {'1': 6}
    assert count_pairs('2 2 3 3 3 4 4 4 4') == {'2': 1, '3': 3, '4': 6}
    print('All tests passed!!!')
