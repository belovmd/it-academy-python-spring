""" Count different numbers

Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.

Пример
Входные данные:
    1 2 3 4 4 4 5
    2 2 4 6 6 6 8
Вывод:
    1 3 5 6 8
Пояснение:
    В первом списке содержатся различные числа: 1 2 3 4 5
    Во втором: 2 4 6 8
    Общие числа из обоих списков: 2 4
    Различные числа из обоих списков: 1 3 5 6 8 - ответ на вопрос "сколько": 5.
"""


set1 = set(input().split())
set2 = set(input().split())
symm_diff = [int(number) for number in set1.symmetric_difference(set2)]
print('Different numbers are: {}, length is {}.'.
      format(symm_diff, len(symm_diff)))
