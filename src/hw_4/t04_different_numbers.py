""" Count different numbers

There are two lists of numbers. Figure out how many different numbers are in
the only one list.

Example:
Input:
    list1: 1 2 2 3 4 5 5 6 7
    List2: 4 5 6 6 8 8 9 0 0 0 0 0
Output:
    7
Explanation:
    Numbers 1, 2, 2, 3, 7 are only in the first list, not in the second.
    Numbers 8, 8, 9, 0, 0, 0, 0, 0 are only in the second list not in
the first.
    There are following different numbers: 1, 2, 3, 7, 8, 9, 0. Total
amount is 7.
"""


set1 = set(input().split())
set2 = set(input().split())
print(len(set1.symmetric_difference(set2)))
