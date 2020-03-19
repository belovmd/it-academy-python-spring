def get_ranges(nmb_list):
    """Get ranges function

    :param nmb_list: list of integers unique numbers
    :return: string of short representation of list
    """
    ranges_lst = [[nmb_list[0]]]
    ranges_ind = 0
    result = []

    for index, element in enumerate(nmb_list[1:]):

        if element == nmb_list[index] + 1:
            ranges_lst[ranges_ind].append(element)
        else:
            ranges_lst.append([element])
            ranges_ind += 1

    for sequence in ranges_lst:
        if len(sequence) == 1:
            result.append('{}'.format(sequence[0]))
        else:
            result.append('{}-{}'.format(sequence[0], sequence[-1]))

    return ', '.join(result)


if __name__ == '__main__':
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
    print(get_ranges([2]))
    print(get_ranges([1, 2, 4, 7, 10, 18]))
