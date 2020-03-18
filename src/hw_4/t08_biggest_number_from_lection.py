""" The biggest number

Yuliya has a list of numbers. Help her to concatenate these numbers as a
strings to get as biggest number as possible.
"""


from functools import cmp_to_key

numbers = ['94', '83', '9', '991', '11', '342', '35', '34274']


def compare_func(x: str, y: str):
    return int(x + y) - int(y + x)


sorted_numbers = sorted(numbers, key=cmp_to_key(compare_func), reverse=True)
print(sorted_numbers, ' or ', ''.join(sorted_numbers))
