"""Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что
любые два элемента, равные друг другу образуют
одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная
пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""

str1 = str(input("Insert string: "))
list2 = []

list1 = str1.split(' ')

for element in list1:
    if element not in list2 and list1.count(element) > 1:
        number_of_couples = \
            (list1.count(element) * (list1.count(element) - 1)) / 2
        print("Element {} : {} coupl(es)"
              .format(element, int(number_of_couples)))
        # exclude element from list1
        list2.append(element)
