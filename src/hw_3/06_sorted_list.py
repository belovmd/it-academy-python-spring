""" Упорядоченный список.

Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок
ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный
список.
"""


def sort_list(lst):
    i = 0
    length = len(lst)
    pos_to_insert = 0
    while i < length:
        if lst[i] != 0:
            if pos_to_insert != i:
                lst[i], lst[pos_to_insert] = lst[pos_to_insert], lst[i]
            pos_to_insert += 1
        i += 1
    return


if __name__ == '__main__':
    # Example
    # list1 = [0, 1, 0, 0, 0, 2, 3, 0, 4, 5, 0, 0]
    # sort_list(list1)
    # print(list1)

    list2 = [0, 1, 0, 2, 0, 0, 0, 3, 0, 4, 5, 6, 0, 0, 0]
    sort_list(list2)
    expected_list2 = [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert list2 == expected_list2, 'Test 1'

    list3 = [1, 2, 3]
    sort_list(list3)
    expected_list3 = [1, 2, 3]
    assert list3 == expected_list3, 'Test 2: nothing to move, no zeros'

    list4 = [0, 0, 0, 0]
    sort_list(list4)
    expected_list4 = [0, 0, 0, 0]
    assert list4 == expected_list4, (
        'Test 3: nothing to move, only zero elements in a list')

    list5 = []
    sort_list(list5)
    expected_list5 = []
    assert list5 == expected_list5, (
        'Test 4: empty list')
