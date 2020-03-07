# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.


def quantity(lst1, lst2):
    common_num = set(lst1).intersection(set(lst2))
    return 'Quantity of common numbers = {}'.format(len(common_num))


print(quantity([1, 2, 3, 4], [1]))
print(quantity([1, 2, 3, 4], [1, 2, 3, 4]))
print(quantity([1, 2, 3, 4], [5, 6, 7, 8]))
print(quantity([], []))
