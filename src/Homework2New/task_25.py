def next_bigger(n):
    """Instructions

    You have to create a function that takes a
    positive integer changing_number and returns the next
    bigger changing_number formed by the same digits.
    If no bigger changing_number can be composed
    using those digits, return -1:
    :param n:integer natural
    :return:integer
    """
    str_number = list(str(n))

    for i in range(len(str_number) - 1, 0, -1):

        if str_number[i] > str_number[i - 1]:
            slice_temp = str_number[i - 1: len(str_number)]
            changing_num = slice_temp.pop(0)
            slice_temp = sorted(slice_temp)

            for j, next_num in enumerate(slice_temp):

                if next_num > changing_num:
                    slice_temp[j] = changing_num
                    slice_temp.insert(0, next_num)
                    break

            return int(''.join(str_number[:i - 1] + slice_temp))

    return -1


assert next_bigger(12) == 21
assert next_bigger(513) == 531
assert next_bigger(2017) == 2071
assert next_bigger(414) == 441
assert next_bigger(144) == 414
assert next_bigger(2389093785) == 2389093857
