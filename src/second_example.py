# List practice
# 1. Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2. Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# 3. Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5. Скопируйте список и добавьте в него элемент '2a'
# такчтобы в исходном списке этого элемента не было.

import  copy

first_list = [a + b for a in "ab" for b in "bcd"]
print(first_list)
print(first_list[::2])

second_list = [a + b for a in "1234" for b in "a"]
print(second_list)
print(second_list.pop(1))

third_list = copy.deepcopy(second_list)
third_list.append('2a')
print(third_list)





