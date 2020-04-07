""" Function to test is biggest_number

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
