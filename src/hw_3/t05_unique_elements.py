""" Вывесли элементы, встречающиеся только один раз

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def count_equal_with_dictionary(elements):
    frequencies = {}
    for element in elements:
        count = frequencies.get(element, 0)
        frequencies[element] = count + 1
    return [element for element, frequency in frequencies.items()
            if frequency == 1]


if __name__ == '__main__':
    elements1 = [1, 1, 1, 2, 3, 4, 5, 3, 3, 0, 3, 3]
    expected1 = [2, 4, 5, 0]
    assert (count_equal_with_dictionary(elements1)) == expected1, (
        'Test 1 dict:  list of integers')

    elements2 = []
    expected2 = []
    assert (count_equal_with_dictionary(elements2)) == expected2, (
        'Test 2 dict: empty list')

    elements3 = 'aaa', 'sss', 1, (3, 55), (3, 55), (3, 80), '42', 'aaa'
    expected3 = ['sss', 1, (3, 80), '42']
    assert (count_equal_with_dictionary(elements3)) == expected3, (
        'Test 3 dict: different element types')

    elements4 = [True, False, 1]
    expected4 = [0]
    assert (count_equal_with_dictionary(elements4)) == expected4, (
        'Test 4 dict: boolean types')
