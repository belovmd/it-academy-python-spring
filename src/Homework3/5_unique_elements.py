"""Unique elements.

5) Уникальные элементы в списке.
Дан список. Выведите те его элементы, которые встречаются в списке только
один раз. Элементы нужно выводить в том порядке, в котором они встречаются
в списке.

"""


def unique_elements(lst):
    """Return unique elements in list"""
    unique_lst = list()
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


if __name__ == '__main__':
    unique_elements([1, 2, 3, 1, 3, 5, 3]) == [2, 5]
    unique_elements([3, 4, 2, 3, 1]) == [4, 2, 1]
    unique_elements(['r', 't', 'r', (1,)]) == ['t', (1,)]
    unique_elements([]) == []
    unique_elements([('a', 'b'), ('a', 'c'), ('a', 'b')]) == [('a', 'c')]
    print('All tests passed!!!')
