"""3 - get ranges
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(lst: list) -> str:
    """get_ranges:
    Take in input list of sorted different numbers and return
    string with ranges these numbers.

    """
    start_range = end_range = lst[0]
    result = []
    for ind, element in enumerate(lst[:-1]):
        if lst[ind + 1] == element + 1:
            end_range = lst[ind + 1]
            if ind + 1 == len(lst) - 1:
                if start_range == end_range:
                    result.append(str(start_range))
                else:
                    result.append(f'{start_range}-{end_range}')
        else:
            if start_range == end_range:
                result.append(str(start_range))
            else:
                result.append(f'{start_range}-{end_range}')
            if ind + 1 == len(lst) - 1:
                result.append(str(lst[ind + 1]))
            start_range = end_range = lst[ind + 1]
    return ','.join(result)


if __name__ == '__main__':
    test_list = [
        [1, 2, 3, 6, 7, 10, 12, 13, 14, 15, 78],
        [0, 1, 2, 3, 4, 7, 8, 10],
        [2, 3, 8, 9],
        [4, 7, 10],
        [3, 5, 7, 8, 9, 10, 13, 14, 15]
    ]
    assert get_ranges(test_list[0]) == "1-3,6-7,10,12-15,78"
    assert get_ranges(test_list[1]) == "0-4,7-8,10"
    assert get_ranges(test_list[2]) == "2-3,8-9"
    assert get_ranges(test_list[3]) == "4,7,10"
    assert get_ranges(test_list[4]) == "3,5,7-10,13-15"
