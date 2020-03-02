""" Посчитать количество пар равных элементов в массиве

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


from collections import Counter
from itertools import combinations


def count_pairs_with_itertools(elements):
    all_combinations = list(combinations(elements, 2))
    equal_pairs = [el for el in all_combinations if el[0] == el[1]]
    return len(equal_pairs)


# Returns the number of combinations C(n,2)
def get_combinations_n_2_count(n):
    return n * (n - 1) // 2


def count_pairs(elements):
    counts = Counter(elements)
    return sum([get_combinations_n_2_count(count) for count
                in counts.values()])


def read_from_input():
    print('Input elements:')
    return list(map(int, input().split()))


if __name__ == '__main__':
    print(count_pairs(read_from_input()))

    elements1 = [1, 1, 1]
    expected_result_1 = 3
    assert(count_pairs(elements1)) == expected_result_1, 'Test 1: three equals'
    assert(count_pairs_with_itertools(elements1)) == expected_result_1, (
        'Test itertools 1: three equals')

    elements2 = [1, 1, 1, 1]
    expected_result_2 = 6
    assert (count_pairs(elements2)) == expected_result_2, 'Test 2: six equals'
    assert (count_pairs_with_itertools(elements2)) == expected_result_2, (
        'Test itertools 2: six equals')

    elements3 = []
    expected_result_3 = 0
    assert (count_pairs(elements3)) == expected_result_3, 'Test 3: empty list'
    assert (count_pairs_with_itertools(elements3)) == expected_result_3, (
        'Test itertools 3: empty list')

    elements4 = [1, 2, 1, 2, 3, 2, 3, 3, 3]
    expected_result_4 = 10
    assert (count_pairs(elements4)) == expected_result_4, (
        'Test 4: three different elements')
    assert (count_pairs_with_itertools(elements4)) == expected_result_4, (
        'Test itertools 4: three different elements')
