def list_practice():
    """List practice tasks"""

    # Generator of the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
    result_list_task_21 = [el1 + el2 for el1 in 'ab' for el2 in 'bcd']
    print(result_list_task_21)

    # Slice for above list to get list ['ab', 'ad', 'bc']
    result_list_task_22 = result_list_task_21[::2]
    print(result_list_task_22)

    # Generator of the list ['1a', '2a', '3a', '4a']
    result_list_task_23 = [str(nmb_el) + 'a' for nmb_el in range(1, 5)]
    print(result_list_task_23)

    # From list above delete item '2a' and print it
    print(result_list_task_23.pop(1))  # task_24

    # copy of above list and insert in it immutable element '2a'
    result_list_task_25 = result_list_task_23[:]
    result_list_task_25.insert(1, '2a')
    print(result_list_task_23, result_list_task_25)


if __name__ == '__main__':
    list_practice()
