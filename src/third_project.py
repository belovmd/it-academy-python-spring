"""Реализовать функцию get_ranges которая получает на вход непустой список

неповторяющихся целых чисел, отсортированных по возрастанию,

которая этот список “сворачивает”

get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"

get_ranges([4,7,10]) // "4,7,10"

get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(source_list: list):
    new_list = list()
    result = str()
    index = 0
    for element in source_list:
        if not new_list or new_list[index][1] + 1 != element:
            new_list.append([element, element])
            index = len(new_list) - 1
        else:
            new_list[index][1] += 1
    index = 0
    for element in new_list:
        if element[index] == element[index + 1]:
            result += '{}, '.format(str(element[index]))
        else:
            result += '{}-{}, '.format(
                str(element[index]),
                str(element[index + 1])
            )
    return result.rstrip(', ')


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
