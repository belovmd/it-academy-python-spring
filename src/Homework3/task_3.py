def tuple_practice():
    """Tuple practice tasks"""

    # Create list ['a', 'b' , 'c'] and tuple from list
    temp_list = list('abc')
    temp_tuple = tuple(temp_list)
    print(temp_tuple)

    # Create tuple (a, b, c) and list from tuple
    temp_tuple = ('a', 'b', 'c', )
    temp_list = list(temp_tuple)
    print(temp_list)

    # multiple assignment in one line
    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    # Create single element tuple
    single_element_tuple = ('123',)
    if len(single_element_tuple) == 1:
        for element in single_element_tuple[0]:
            print(element, end=' ')


if __name__ == '__main__':
    tuple_practice()
