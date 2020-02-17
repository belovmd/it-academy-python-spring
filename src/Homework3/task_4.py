def pairs_of_element(input_string):
    """Count of pairs of elements

    :param input_string: string of numbers divided by whitespaces
    :return: numbers of pairs of equal elements
    """
    count = 0
    list_of_numbers = [int(char) for char in input_string.split()]

    for start_ind, first_el in enumerate(list_of_numbers):
        for _, second_el in enumerate(list_of_numbers[start_ind + 1::]):
            if first_el == second_el:
                count += 1
    return count


if __name__ == '__main__':

    assert (pairs_of_element('   1      1    1   ')) == 3
    assert (pairs_of_element('1 1 1 1')) == 6
    assert (pairs_of_element('1 2 3 4 5')) == 0
    assert (pairs_of_element('12 5 9 12432455 6 12')) == 1
    assert (pairs_of_element('1 1 1 1 1 1 1 1 1')) == 36
    print(pairs_of_element(input('Enter test string: ')))
