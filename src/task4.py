# Даны два списка чисел. Посчитайте, сколько различных чисел входит только
# в один из этих списков


def quantity(lst1, lst2):
    lst1, lst2 = set(lst1), set(lst2)
    lst1.symmetric_difference_update(lst2)
    return 'Quantity of different numbers = {}'.format(lst1)


print(quantity([1, 2, 3, 4], [1]))
print(quantity([1, 2, 3, 4], [1, 2, 3, 4]))
print(quantity([1, 2, 3, 4], [5, 6, 7, 8]))
print(quantity([], []))
