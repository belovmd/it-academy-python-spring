def frequency_sort(items):
    """Sorts

    Sort the given iterable so that its elements end up in the decreasing
    frequency order, that is, the number of times they appear in elements
    :param items: list of elements of string or integer type
    :return: sorted list with elements frequency key
    """
    dict_count, result = dict.fromkeys(items, 0), []
    for item in items:
        dict_count[item] += 1
    sorted_items = sorted(dict_count,
                          key=lambda x: (-dict_count[x], items.index(x)))
    for item in sorted_items:
        for _ in range(dict_count[item]):
            result.append(item)
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    assert list(frequency_sort(
        [4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(
        ['bob', 'bob', 'carl', 'alex', 'bob'])) == \
        ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
