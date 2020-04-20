"""Даны два списка чисел. Посчитайте, сколько различных чисел входит

только в один из этих списков.

"""

first_list = [1, 6, 4, 7, 3, 84, 2, 2, 654, 2, 67, 42]
second_list = [5, 3, 2, 1, 6, 3, 73, 32, 63]
result = set(first_list)
result.symmetric_difference(second_list)
print(len(result))
