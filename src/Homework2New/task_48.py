def seven_segment(lit_seg, broken_seg):
    """Two displays with seven segment screen

    :param lit_seg: Contains the lit segments as a set of
    letters representing segments
    :param broken_seg: Contains the broken segments as a set of
    letters representing segments
    :return: The total number that the device may be displaying
    """
    nmb_dict = {1: {'B', 'C'},
                2: {'A', 'B', 'D', 'E', 'G'},
                3: {'A', 'B', 'C', 'D', 'G'},
                4: {'B', 'C', 'F', 'G'},
                5: {'A', 'C', 'D', 'F', 'G'},
                6: {'A', 'C', 'D', 'E', 'F', 'G'},
                7: {'A', 'B', 'C'},
                8: {'A', 'B', 'C', 'D', 'E', 'F', 'G'},
                9: {'A', 'B', 'C', 'D', 'F', 'G'},
                0: {'A', 'B', 'C', 'D', 'E', 'F'}}

    first_segment_set = [set(), set()]
    second_segment_set = [set(), set()]

    nmb_of_first_segment_list = []
    nmb_of_second_segment_list = []

    for element in lit_seg:
        if element.isupper():
            first_segment_set[0].add(element)
            first_segment_set[1].add(element)
        else:
            second_segment_set[0].add(element.upper())
            second_segment_set[1].add(element.upper())
    for element in broken_seg:
        if element.isupper():
            first_segment_set[1].add(element)
        else:
            second_segment_set[1].add(element.upper())

    for key, value in nmb_dict.items():
        if first_segment_set[0] <= value <= first_segment_set[1]:
            nmb_of_first_segment_list.append(key)
        if second_segment_set[0] <= value <= second_segment_set[1]:
            nmb_of_second_segment_list.append(key)

    f_segment = len(nmb_of_first_segment_list)
    s_segment = len(nmb_of_second_segment_list)

    if f_segment > 0 and s_segment > 0:
        return f_segment * s_segment
    elif f_segment > 0:
        return f_segment
    elif s_segment > 0:
        return s_segment
    return 0


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment(
        ({'B', 'C', 'a', 'f', 'g', 'c', 'd'},
         {'A', 'G', 'D', 'e'}) == 6)
    assert seven_segment(
        ({'B', 'C', 'a', 'f', 'g', 'c', 'd'},
         {'A', 'G', 'D', 'F', 'b', 'e'}) == 20)
    print('"Run" is good. How is "Check"?')
