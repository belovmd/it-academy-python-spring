"""Given an array, find the integer that appears
an odd number of times. There will always be only one integer that
appears an odd number of times.
sample test:
test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);
test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);
"""


def find_it(seq):
    for elem in seq:
        if seq.count(elem) % 2 != 0:
            return elem
