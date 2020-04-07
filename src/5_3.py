"""Реализовать функцию get_ranges,
которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
 // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    segment = 0
    lst_temp = [[]]
    final_str = ''

    for number in range(len(lst)):
        if number != len(lst) - 1:
            if lst[number] + 1 == lst[number + 1]:
                lst_temp[segment].append(lst[number])
            else:
                lst_temp.append([])
                lst_temp[segment].append(lst[number])
                segment += 1
        else:
            lst_temp[segment].append(lst[number])

    for element in lst_temp:
        if len(element) > 1:
            final_str += str(element[0]) + '-' + str(element[-1]) + ', '
        else:
            final_str += str(element[0]) + ', '

    final_str = final_str.rstrip(', ')

    return final_str


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
