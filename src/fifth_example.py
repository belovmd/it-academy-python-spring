"""Уникальные элементы в списке

Дан список. Выведите те его элементы,

которые встречаются в списке только один раз.

Элементы нужно выводить в том порядке, в котором они встречаются в списке.

"""

# 5 - 4 - 7 - 9 - dino

symbol_list = [1, 2, 3, 2, 5, 2, 4, 3, 7, 2, 9, 1, 'string', 'dino', 'string']
symbol_dict = dict()
for elem in symbol_list:
    symbol_dict[elem] = symbol_dict.get(elem, 0) + 1
symbol_list.clear()
for symbol, quantity in symbol_dict.items():
    if quantity == 1:
        symbol_list.append(symbol)
print(symbol_list)
