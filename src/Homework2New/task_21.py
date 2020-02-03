def simple_nod(number):
    """Instructions

    Quick find of simple dividers
    for numbers
    """
    nod = 2
    temp_list = []
    while nod ** 2 <= number:
        if not number % nod:
            temp_list.append(nod)
            number //= nod
        else:
            nod += 1
    if number > 1:
        temp_list.append(number)
    return temp_list


def sum_for_list(lst):
    """Instructions

    Given an array of positive or negative integers
    I= [i1,..,in]
    you have to produce a sorted array P of the form
    [ [p, sum of all ij of I for which p is a prime
    factor (p positive) of ij] ...]
    P will be sorted by increasing order of the prime
    numbers. The final result has to be given as a
    string in Java, C#, C, C++ and as an array of
    arrays in other languages.
    Example:
    I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
    :param lst: integers numbers
    :return: sequence of lists
    """
    list_of_nods = []
    for num in lst:
        temp_list = simple_nod(abs(num))
        for item in temp_list:
            if item not in list_of_nods:
                list_of_nods.append(item)
    result = []
    for nod in list_of_nods:
        flag = False
        sum = 0
        for num in lst:
            if not num % nod:
                sum += num
                flag = True
        if flag:
            result.append([nod, sum])
    return sorted(result, key=lambda x: x[0])


if __name__ == '__main__':
    test_list = [12, 15]
    assert sum_for_list(test_list) == [[2, 12], [3, 27], [5, 15]]
