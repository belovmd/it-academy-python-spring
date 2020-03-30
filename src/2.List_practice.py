import copy
# 1) Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2) Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# 3) Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# 4) Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5) Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
# списке этого элемента не было.
lst1 = [a + b for a in 'ab' for b in 'bcd']
print(lst1)
lst2 = lst1[::2]
print(lst2)
lst3 = [num + 'a' for num in '1234']
print(lst3)
print([el for el in lst3 if el != '2a'])
lst3 = [el for el in lst3 if el != '2a']
lst4 = copy.deepcopy(lst3)
lst4.append('2a')
print('List3 = {}\nList4 = {}'.format(lst3, lst4))
