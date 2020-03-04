def common_numbers(lst1, lst2):
    """Unique elements from each list common for two lists

    :param lst1: list with integers numbers
    :param lst2: list with integers numbers
    :return: number of unique elements common for two lists
    """
    dict_count = {}
    for nmb in lst1 + lst2:
        dict_count[nmb] = dict_count.get(nmb, 0) + 1
    counter = 0
    common_elements = {*lst1} & {*lst2}
    for key, value in dict_count.items():
        counter += 1 if value == 2 and key in common_elements else 0
    return counter


def different_numbers(lst1, lst2):
    """Unique elements from each list unique for two lists

    :param lst1: list with integers numbers
    :param lst2: list with integers numbers
    :return: number of unique elements from each list unique for two lists
    """
    dict_count = {}
    for nmb in lst1 + lst2:
        dict_count[nmb] = dict_count.get(nmb, 0) + 1
    counter = 0
    common_elements = {*lst1} & {*lst2}
    for key, value in dict_count.items():
        counter += 1 if value == 1 and key not in common_elements else 0
    return counter


if __name__ == '__main__':
    lst1 = [1, 2, 2, 4, 5, 7, 7, 9, 12]
    lst2 = [2, 3, 3, 4, 5, 5, 7, 9, 10, 11]
    assert common_numbers(lst1, lst2) == 2
    assert different_numbers(lst1, lst2) == 4
