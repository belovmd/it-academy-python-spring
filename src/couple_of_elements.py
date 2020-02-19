# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
elements = '1 1 2 2 2 1 5 7'
elements = elements.split()
dct1 = {}
for el in elements:
    dct1[el] = elements.count(el)
print(dct1)
list_of_couples = [(el * (el - 1)) / 2 for el in dct1.values() if el > 1]
number_of_couples = int(sum(list_of_couples))
print(number_of_couples)
