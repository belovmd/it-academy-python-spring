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
list_temp = []

list1 = str1.split(' ')

for number in range(len(list1)):
    list1[number] = int(list1[number])

list1.sort()

list2 = list1.copy()
list2.reverse()

for element in list1:
    if element not in list_temp:

        number_of_element = \
            len(list1) - list2.index(element) - list1.index(element)

        number_of_couples = \
            (number_of_element * (number_of_element - 1)) / 2

        print("Element {} : {} coupl(es)"
              .format(element, int(number_of_couples)))
        list_temp.append(element)
