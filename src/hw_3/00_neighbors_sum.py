""" Посчитать сумму двух соседних элементов списка

Нaпишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его
cоседей. Для элeментов списка, являющиxся крайними, одним из соседей считается
элемент, находящий на противоположном конце этого списка. Например, если на
вход подаётся cписок «1 3 5 6 10», то на выход ожидается cписок «13 6 9 15 7».
Если на вход пришло только однo число, надо вывести его же. Вывoд должен
содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.
"""


def calculate_neighbors_sum(a):
    b = []
    if a:
        if len(a) == 1:
            b.append(a[0])
        else:
            # For 0-index of a list:
            b.append(a[1] + a[-1])

            # For a middle of a list:
            index = 1
            length = len(a)
            while index < length:
                if index < len(a) - 1:
                    b.append(a[index - 1] + a[index + 1])
                index += 1

            # For the last element of a list:
            b.append(a[0] + a[-2])
    return b


if __name__ == '__main__':
    assert(calculate_neighbors_sum([])) == [], 'Test 1 - empty list'
    assert(calculate_neighbors_sum([1])) == [1], 'Test 2 - one element'
    assert(calculate_neighbors_sum([1, 2])) == [4, 2], 'Test 3 - two elements'
    assert(calculate_neighbors_sum([1, 3, 5, 6, 10])) == [13, 6,
                                                          9, 15, 7], 'Test 4'

    print('Input line of integers:')
    lst = list(map(int, input().split()))
    print(*calculate_neighbors_sum(lst))
