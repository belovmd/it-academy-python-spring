"""List practice
1. Используйте генератор списков чтобы получить
следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы
получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить
следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из
прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент
'2a' так чтобы в исходном списке этого элемента
не было."""


import copy

list0 = ['a', 'b', 'c', 'd']
list1 = [element1 + element2 for element1 in list0[0:2] for element2 in list0[1:4]]
# "end" of slice not included!!!!!!!!!!!!!!!!!!!
print(list1)

list2 = list1[0::2]
print(list2)

list3 = [str(number) + 'a' for number in range(1, 5)]
print(list3)

list3.remove('2a')
print(list3)

list4 = copy.copy(list3)
list4.append('2a')
print(list4)