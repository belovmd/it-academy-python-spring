""" Function to test is biggest_number


By my mistake I used wrong function for writing tests. I decided not to delete
this file and test (test_biggest_number.py) from a homework #6.

Task that a function solves:
Yuliya has a list of numbers. Help her to concatenate these numbers as a
strings to get as biggest number as possible.
"""


from functools import cmp_to_key


def biggest_number(numbers):
    def compare_func(x: str, y: str):
        return int(x + y) - int(y + x)

    sorted_numbers = sorted(numbers, key=cmp_to_key(compare_func),
                            reverse=True)
    return ''.join(sorted_numbers)
