# Задача 1 (FizzBuzz)
for x in range(1, 100):
    s = ''
    if x % 3 == 0:
        s += 'Fizz'
    if x % 5 == 0:
        s += "Buzz"
    if s == '':
        s = x
    print(s, end=' ')

# Задача 2 (List practice)
a = [a + b for a in 'ab' for b in 'bcd'][::2]
print(a)

s = [s + i for s in '1234' for i in 'a']
del s[1]
print(s)
i = s.copy()
i.append('2a')
print(i)

# Задача 3 (Tuple practice)
lst = ['a', 'b', 'c']
lst = tuple(lst)

tpl = ('a', 'b', 'c')
tpl = list(tpl)

a, b, c = 'a', 2, 'python'

tuple_new = ([1, 2, 3],)
print('len = ', len(tuple_new))
for element in tuple_new[0]:
    print(element)
# Задача 4 (Пары элементов)

"""Дан список чисел. Посчитайте, сколько в нем пар элементов,

равных друг другу.

Считается, что любые два элемента,

равные друг другу образуют одну пару, которую необходимо посчитать.

Входные данные - строка из чисел, разделенная пробелами.

Выходные данные - количество пар.

Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count(num_string):
    el = dict()
    for element in num_string.split():
        el[element] = el.get(element, 0) + 1
    for elem, count in el.items():
        el[elem] = 0
        for item in range(count):
            for _ in range(item + 1, count):
                el[elem] += 1
    return el


if __name__ == '__main__':
    assert count('1 1 1 1') == {'1': 6}
    assert count('2 2 3 3 3 4 4 4 4') == {'2': 1, '3': 3, '4': 6}
    print('All tests passed!!!')


# 5 Уникальные элементы в списке

def unique_elements(lst):
    unique_lst = list()
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


if __name__ == '__main__':
    unique_elements([1, 2, 3, 1, 3, 5, 3]) == [2, 5]
    unique_elements([3, 4, 2, 3, 1]) == [4, 2, 1]
    unique_elements(['r', 't', 'r', (1,)]) == ['t', (1,)]
    unique_elements([]) == []
    unique_elements([('a', 'b'), ('a', 'c'), ('a', 'b')]) == [('a', 'c')]
    print('All tests passed!!!')


# 6Упорядоченный список

def list(lst):
    for ind in range(len(lst) - 1, -1, -1):
        if lst[ind] == 0:
            lst.append(lst.pop(ind))
    return lst


if __name__ == '__main__':
    assert list([1, 0, 2, 0, 3, 0, 4]) == [1, 2, 3, 4, 0, 0, 0]
    assert list([0, 0, 0, 1, 0, 2, 0]) == [1, 2, 0, 0, 0, 0, 0]
    assert list([1, 0, 0, 0, 0, 0, 2]) == [1, 2, 0, 0, 0, 0, 0]
    assert list([0, 0, 0, 1, 0, 0, 0]) == [1, 0, 0, 0, 0, 0, 0]
    print('All tests passed!!!')
