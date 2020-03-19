""" Collapse ranges

Implement get_ranges function with following input parameters:
a non-empty list of non-repeated integers, sorted in ascending order. Function
should collapse input list in a way below:
   get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) -> "0-4,7-8,10"
   get_ranges([4,7,10]) -> "4,7,10"
   get_ranges([2, 3, 8, 9]) -> "2-3,8-9"
"""


def get_ranges(lst):
    ranges = []
    for number in lst:
        if not ranges or number != ranges[-1][-1] + 1:
            # start a new interval
            ranges.append([])
        # append to the last interval
        ranges[-1].append(number)

    return ','.join([str(interval[0])
                     if interval[0] == interval[-1]
                     else str(interval[0]) + '-' + str(interval[-1])
                     for interval in ranges])


if __name__ == '__main__':
    assert get_ranges([1, 2, 3, 4, 5, 6, 7, 8]) == '1-8', 'Test 0'
    assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == '0-4,7-8,10', 'Test 1'
    assert get_ranges([4, 7, 10]) == '4,7,10', 'Test 2'
    assert get_ranges([2, 3, 8, 9]) == '2-3,8-9', 'Test 3'
    assert get_ranges([2, 4]) == '2,4', 'Test 4'
    assert get_ranges([2, 3]) == '2-3', 'Test 5'
    assert get_ranges([1]) == '1', 'Test 6'
