# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz


def fizz_buzz():
    for i in range(1, 101):
        WhatPrint = ""
        if i % 3 == 0:
            WhatPrint += "Fizz"
        if i % 5 == 0:
            WhatPrint += "Buzz"
        if WhatPrint == "":
            WhatPrint = i
        print(WhatPrint)


# ----------------------------------------------------------------------
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так
# чтобы в исходном списке этого элемента не было.
def list_practice():
    list1 = [element + element2 for element in "ab" for element2 in "bcd"]
    print(list1)
    print(list1[::2])
    list2 = [element + 'a' for element in "1234"]
    print("list2 = {}".format(list2))
    print("{}, list2 = {}".format(list2.pop(list2.index('2a')), list2))
    list3 = list2.copy()
    list3.append("2a")
    print("list2 = {}, list3 = {}".format(list2, list3))


# ----------------------------------------------------------------------
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает
def tuple_practice():
    lst = ['a', 'b', 'c']
    tpl = tuple(lst)
    print(tpl)
    lst = [element for element in tpl]
    print(lst)
    a, b, c = 'a', 'b', 'python'
    print(a, b, c)
    tpl = ("123",)
    print("{}, len = {}".format(tpl, len(tpl)))
    for i in tpl[0]:
        print(i, end=" ")


# ----------------------------------------------------------------------
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Входные данные - строка из чисел,
# разделенная пробелами. Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
def pairs_of_elements(stroka):
    ret_dict = {}
    list = stroka.split()
    for i in list:
        if not i in ret_dict:
            kol_el = list.count(i)
            if kol_el > 1:
                ret_dict[i] = kol_el * (kol_el - 1) / 2
    print(ret_dict)


# ----------------------------------------------------------------------
# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.
def unique_elements(list):
    for i in list:
        if list.count(i) == 1:
            print(i, end=" ")


# ----------------------------------------------------------------------
# Дан список целых чисел. Требуется переместить все ненулевые элементы
# в левую часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
def ordered_list(list):
    index = len(list) - 1
    while index >= 0:
        if list[index] == 0:
            list.append(list.pop(index))
        index -= 1
    print(list)


# fizz_buzz()
# list_practice()
# tuple_practice()
# pairs_of_elements("1 2 5 9 1 36 8 5 9 6 1 9 4 3 5 8 9 1 1")
# unique_elements([7,2,4,5,7,4])
ordered_list([0, 1, 5, 0, 0, 5, 7, 9, 0, 0])
