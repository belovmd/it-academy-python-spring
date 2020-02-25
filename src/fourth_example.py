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
dict_number = {element: list_number.count(element) for element in list_number}
dict_number = {key: int(dict_number.get(key) * (dict_number.get(key) - 1) / 2)
               for key in dict_number}
print(dict_number)
print("sum pairs: {}".format(sum(dict_number.values())))
