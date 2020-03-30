def pairs_of_element(input_string):
    """Count of pairs of elements

    :param input_string: string of numbers divided by whitespaces
    :return: numbers of pairs of equal elements
    """
    count = 0
    list_of_numbers = [int(char) for char in input_string.split()]

    el_dict = {}
    for element in list_of_numbers:
        el_dict[element] = el_dict.get(element, 0) + 1
        count += el_dict[element] - 1
    return count


if __name__ == '__main__':

    assert (pairs_of_element(' 3  1   4   1  3  1   2 2')) == 5
    assert (pairs_of_element('1 1 1 1')) == 6
    assert (pairs_of_element('1 2 3 4 5')) == 0
    assert (pairs_of_element('12 5 9 12432455 6 12')) == 1
    assert (pairs_of_element('1 1 1 1 1 1 1 1 1')) == 36
    print(pairs_of_element(input('Enter test string: ')))
