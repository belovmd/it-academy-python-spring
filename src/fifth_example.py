"""Уникальные элементы в списке

Дан список. Выведите те его элементы,

которые встречаются в списке только один раз.

Элементы нужно выводить в том порядке, в котором они встречаются в списке.

"""

# 5 - 4 - 7 - 9 - dino
singe_list = [1, 2, 3, 2, 5, 2, 4, 3, 7, 2, 9, 1, 'string', 'dino', 'string']

for element in singe_list:
    if singe_list.count(element) == 1:
        print(element)

print([element for element in singe_list if singe_list.count(element) == 1])
