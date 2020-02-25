def unique_elements(input_list):
    """Unique elements - common solution

    This algorithm has O(N**2) asymptotic but works with all types of elements
    :param input_list: list of elements
    :return: list of unique element of input_list
    """
    return [el for el in input_list if input_list.count(el) == 1]


def unique_elements_spec(input_list):
    """Unique elements - special solution

    This algorithm has less asymptotic but works only if list consists
    from immutable elements
    :param input_list: list of IMMUTABLE elements
    :return: list of unique element of input_list
    """
    dict_count = {}
    for element in input_list:
        dict_count[element] = dict_count.get(element, 0) + 1
    return [key for key, value in dict_count.items() if value == 1]


if __name__ == '__main__':

    assert unique_elements([1, 2, 3, [], []]) == [1, 2, 3]
    assert unique_elements([1, 1, 1, 1, 1]) == []
    assert unique_elements([]) == []
    assert unique_elements([[1], [2], [3], []]) == [[1], [2], [3], []]
    assert unique_elements_spec([2, (1, 2, ), 3, 4]) == [2, (1, 2, ), 3, 4]
    assert unique_elements_spec([2, (1, 2, ), (1, )]) == [2, (1, 2, ), (1, )]
    assert unique_elements_spec([(1, ), (1, 2, ), (1, )]) == [(1, 2, )]
    assert unique_elements_spec(['1', 1, (1, )]) == ['1', 1, (1, )]
