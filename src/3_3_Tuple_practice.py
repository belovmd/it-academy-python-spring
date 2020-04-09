"""Tuple practice
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2,
c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании
по этому элементы последовательно выводились значения
1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""

list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print(tuple1)

tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print(list2)

a, b, c = 'a', 2, 'python'

ele = (1, 2, 3)
tuple3 = (ele,)

for element in tuple3:
    for elements in element:
        print(elements)

print(len(tuple3))
