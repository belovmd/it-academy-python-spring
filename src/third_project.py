"""Реализовать функцию get_ranges которая получает на вход непустой список

неповторяющихся целых чисел, отсортированных по возрастанию,

которая этот список “сворачивает”

get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"

get_ranges([4,7,10]) // "4,7,10"

get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(lst):
    lst_index = []
    while lst:
        interval = [el for i, el in enumerate(lst) if el == lst[0] + i]
        if len(interval) == 1:
            lst_index.append(str(interval[0]))
        else:
            lst_index.append('{} - {}'.format(interval[0], interval[-1]))
        lst = lst[len(interval):]
    return ', '.join(lst_index)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
