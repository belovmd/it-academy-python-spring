""" Count different numbers

Caunt all different numbers from two lists of numbers.

Input:
List of numbers
List of numbers

Output:
a number

Example:
Input:
    1 2 3 4 4 4 5
    2 2 4 6 6 6 8
Output:
    2
Explanation:
   These two lists has following common numbers:
   2, 2, 2, 4, 4, 4, 4
   There are only 2 different numbers: 2, 4.
"""


set1 = set(input().split())
set2 = set(input().split())
print(len(set1.intersection(set2)))