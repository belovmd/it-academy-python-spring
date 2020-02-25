# Tuple practice
# 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# 3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4. Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

convert_list = ['a', 'b', 'c']
print(convert_list, type(convert_list))
convert_list = tuple(convert_list)
print(convert_list, type(convert_list))

convert_tuple = ('a', 'b', 'c')
print(convert_tuple, type(convert_tuple))
convert_tuple = list(convert_tuple)
print(convert_tuple, type(convert_tuple))

a, b, c = 'a', 2, 'python'
print('a = {}, b = {}, c = {}'.format(a, b, c))

my_tuple = ([1, 2, 3],)
print('Length = {}'.format(len(my_tuple)))
for element in my_tuple[0]:
    print(element)
