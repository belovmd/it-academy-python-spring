"""List practice"""

"""
2.1) Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""
result_2_1 = [x + y for x in 'ab' for y in 'bcd']
print(result_2_1)

"""
2.2) Используйте на предыдущий список slice, чтобы получить следующий:
['ab', 'ad', 'bc'].
"""
result_2_2 = result_2_1[::2]
print(result_2_2)

"""
2.3) Используйте генератор списков чтобы получить следующий:
 ['1a', '2a', '3a', '4a'].
"""
result_2_3 = [char + 'a' for char in '1234']
print(result_2_3)

"""
2.4) Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
"""
result_2_4 = result_2_3.pop(1)
print(result_2_4)

"""
2.5) Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
списке этого элемента не было.
"""
some_list = ['1a', '3a', '4a']
copy_list = some_list.copy()
copy_list.insert(1, '2a')
print(some_list)
print(copy_list)
