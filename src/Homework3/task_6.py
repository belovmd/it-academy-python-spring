def ordered_list(input_list):
    """Ordered list

    :param input_list: list of integers
    :return: sorted list where all 0 elements in the end of list
    """
    el_index, iter_count = 0, len(input_list)

    while iter_count > 0:
        if not input_list[el_index]:
            input_list.append(input_list.pop(el_index))
        else:
            el_index += 1
        iter_count -= 1
    return input_list


if __name__ == '__main__':
    assert ordered_list([1, 2, 0, 0, 4, 0, 3, 1]) == [1, 2, 4, 3, 1, 0, 0, 0]
    assert ordered_list([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert ordered_list([0]) == [0]
    assert ordered_list([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert ordered_list([0, 0, 0, 0, 1, 2, 3, 4]) == [1, 2, 3, 4, 0, 0, 0, 0]
    assert ordered_list([1, 2, 3, 4, 0, 5]) == [1, 2, 3, 4, 5, 0]
    assert ordered_list([0, 1, 2, 3, 4]) == [1, 2, 3, 4, 0]
    assert ordered_list([]) == []
    print(ordered_list([1, 2, 0, 0, 4, 0, 3, 1]))
