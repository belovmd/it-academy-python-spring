# Уникальные элементы в списке
# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
lis = [1, 2, 3, 2, 3, 1, 6, 3, 2, 1]
x = []
[print(x) for x in lis if lis.count(x) == 1]
