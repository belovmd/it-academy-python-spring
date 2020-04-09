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

list0 = 'abcd'
list1 = [element1 + element2 for element1 in list0[0:2]
         for element2 in list0[1:4]]

print(list1)

list2 = list1[0::2]
print(list2)

list3 = [element + 'a' for element in '1234']
print(list3)

print(list3.pop(list3.index('2a')))

list4 = copy.copy(list3)
list4.append('2a')
print(list4)
print(list3)
