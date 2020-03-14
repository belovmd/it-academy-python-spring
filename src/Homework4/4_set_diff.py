"""Задача 4

Даны два списка чисел. Посчитайте, сколько различных чисел входит только в
один из этих списков.

"""
lst1 = [1, 2, 3, 2, 4, 5]
lst2 = [2, 6, 3, 7]
count_diff_elem_lst1 = len(set(lst1) - set(lst2))
count_diff_elem_lst2 = len(set(lst2) - set(lst1))
print(f'Count different elements contains only in '
      f'list 1: {count_diff_elem_lst1}')
print(f'Count different elements contains only in '
      f'list 2: {count_diff_elem_lst2}')
