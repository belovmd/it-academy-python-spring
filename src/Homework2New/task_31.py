def checkio(data: list) -> list:
    """Non - unique numbers

    :param data: list of integers
    :return: list of integers with non-unique numbers in data
    """

    dict_count = dict.fromkeys(data, 0)
    for element in data:
        dict_count[element] += 1
    return [element for element in data if dict_count[element] > 1]


if __name__ == "__main__":

    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert list(checkio([1, 2, 3, 4, 5])) == []
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
    print("It is all good. Let's check it now")
