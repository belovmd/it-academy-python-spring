# 3 --------------------------------------------------------------------------
# Реализовать функцию get_ranges которая получает на вход непустой список
# неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


# create list from lists new_lst[[elem1, elem2], ....]
def get_ranges(lst):
    new_lst = []
    index_new_lst = 0
    for elem in lst:
        if not new_lst or new_lst[index_new_lst][1] + 1 != elem:
            new_lst.append([elem, elem])
            index_new_lst = len(new_lst) - 1
        else:
            new_lst[index_new_lst][1] += 1
    # create and return string from list
    for ind, elem in enumerate(new_lst):
        if elem[0] == elem[1]:
            new_lst[ind] = str(elem[0])
        else:
            new_lst[ind] = str(elem[0]) + "-" + str(elem[1])
    return ",".join(new_lst)


# "0-4,7-8,10"
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
# "4,7,10"
print(get_ranges([4, 7, 10]))
# "2-3,8-9"
print(get_ranges([2, 3, 8, 9]))
