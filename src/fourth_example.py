"""Пары элементов

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

Считается, что любые два элемента, равные друг другу образуют одну пару,

которую необходимо посчитать.

Входные данные - строка из чисел, разделенная пробелами.

Выходные данные - количество пар.

Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

"""

string_number = '1 2 3 4 5 1 2 3 5 3 7 4 2 1 6 4 3 7 2 4 1 3 6 5 4 2 6'
list_number = string_number.split()
list_number.sort()
dict_pairs = dict()
for elem in list_number:
    dict_pairs[elem] = dict_pairs.get(elem, 0) + 1
for key in dict_pairs:
    dict_pairs[key] = int(dict_pairs.get(key) * (dict_pairs.get(key) - 1) / 2)
print(dict_pairs)
print("sum pairs: {}".format(sum(dict_pairs.values())))
