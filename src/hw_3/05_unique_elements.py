""" Вывесли элементы, встречающиеся только один раз

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


from collections import Counter


def count_equal_elements(elements):
    counts = Counter(elements)
    return [element for element, value in counts.items() if value == 1]


def count_equal_with_dictionary(elements):
    dict_from_elements = {}
    for el in elements:
        count = dict_from_elements.get(el, 0)
        dict_from_elements[el] = count + 1
    return [key for key, value in dict_from_elements.items() if value == 1]


if __name__ == '__main__':
    # Example:
    print(count_equal_elements([3, 3, 4, 3, 5, 8]))
    print(count_equal_with_dictionary([3, 3, 4, 3, 5, 8]))

    elements1 = [1, 1, 1, 2, 3, 4, 5, 3, 3, 0, 3, 3]
    expected1 = [2, 4, 5, 0]
    assert(count_equal_elements(elements1)) == expected1, (
        'Test 1: list of integers')
    assert (count_equal_with_dictionary(elements1)) == expected1, (
        'Test 1 dict:  list of integers')

    elements2 = []
    expected2 = []
    assert(count_equal_elements(elements2)) == expected2, (
        'Test 2: empty list')
    assert (count_equal_with_dictionary(elements2)) == expected2, (
        'Test 2 dict: empty list')

    elements3 = 'aaa', 'sss', 1, (3, 55), (3, 55), (3, 80), '42', 'aaa'
    expected3 = ['sss', 1, (3, 80), '42']
    assert(count_equal_elements(elements3)) == expected3, (
        'Test 3: different element types')
    assert (count_equal_with_dictionary(elements3)) == expected3, (
        'Test 3 dict: different element types')

    elements4 = [True, False, 1]
    expected4 = [0]
    assert(count_equal_elements(elements4)) == expected4, (
        'Test 4: boolean types')
    assert (count_equal_with_dictionary(elements4)) == expected4, (
        'Test 4 dict: boolean types')
