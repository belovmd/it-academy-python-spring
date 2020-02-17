"""Tuple practice"""

"""
3.1) Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
"""
print(tuple(list('abc')))
# ----------------------------------------------------------------
"""
3.2) Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
"""
print(list(tuple('abc')))
# ----------------------------------------------------------------
"""
3.3) Сделайте следующие присвоения одной строкой a = 'a', b=2, c='python'.
"""
a, b, c = 'a', 2, 'python'
print('{a}, {b}, {c}'.format(a=a, b=b, c=c))
# ----------------------------------------------------------------
"""
3.4) Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементу последовательно выводились значения 1, 2, 3. Убедитесь что len() 
исходного кортежа возвращает 1
"""
tuple_new = ([1, 2, 3],)
print('len = ', len(tuple_new))
for element in tuple_new[0]:
    print(element)
# -----------------------------------------------------------------
