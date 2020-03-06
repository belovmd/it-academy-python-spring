def common_numbers(lst1, lst2):
    """Different elements common for two lists

    :param lst1: list with integers numbers
    :param lst2: list with integers numbers
    :return: number of different elements common for two lists
    """
    return len({*lst1} & {*lst2})


def different_numbers(lst1, lst2):
    """Different elements not common for two lists

    :param lst1: list with integers numbers
    :param lst2: list with integers numbers
    :return: number of different elements not common for two lists
    """
    return len({*lst1} ^ {*lst2})


if __name__ == '__main__':
    lst1 = [1, 2, 2, 4, 5, 7, 7, 9, 12]
    lst2 = [2, 3, 3, 4, 5, 5, 7, 9, 10, 11]
    assert common_numbers(lst1, lst2) == 5
    assert different_numbers(lst1, lst2) == 5
