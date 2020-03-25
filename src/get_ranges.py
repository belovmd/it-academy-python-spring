"""3. Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst=[0]):
    new_lst = []
    first = second = lst[0]
    for elem in lst:
        if second + 1 == elem:
            second = elem
        elif second + 1 < elem:
            if first == second:
                new_lst.append(str(first))
            else:
                new_lst.append(str(first) + '-' + str(second))
            first = second = elem
    if first == second:
        new_lst.append(str(first))
    else:
        new_lst.append(str(first) + '-' + str(second))
    print(new_lst)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # 0-4, 7-8, 10
get_ranges([4, 7, 10])  # 4, 7, 10
get_ranges([2, 3, 8, 9])  # 2-3, 8-9
