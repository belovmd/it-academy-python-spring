# 1. Dict comprehensions
# Создайте словарь с помощью генератора словарей, так чтобы его ключами
# были числа от 1 до 20, а значениями кубы этих чисел.
def dict_comprehensions():
    dict = {el: el ** 3 for el in range(1, 21)}
    return dict


# -----------------------------------------------------------------------------
# 2 Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия
# городов этой страны. В следующей строке записано число M, далее
# идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны,
# в котором находится данный город.
def cities(str_country_cities):
    list_str = str_country_cities.split("\n")
    dict_cities = dict()
    list_countrys = ["нет страны для города в базе данных."]
    n = 0
    for stroka in list_str:
        if stroka.isdigit():
            if n > 0:
                n = -1
        elif n > 0 and stroka:
            lists = stroka.split()
            for inds, s in enumerate(lists):
                if inds == 0:
                    list_countrys.append(s)
                else:
                    dict_cities[s] = n
        elif stroka:
            print(stroka, " => ", list_countrys[dict_cities.get(stroka, 0)])
        if n >= 0:
            n += 1


# -----------------------------------------------------------------------------
# 3
# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.
def two_list(str1, str2):
    set1 = set(str1.split())
    set1.update(set(str2.split()))
    return len(set1)


# -----------------------------------------------------------------------------
# 4
# Даны два списка чисел. Посчитайте, сколько различных чисел
# входит только в один из этих списков
def count_different(str1, str2):
    set1 = set(str1.split())
    set1.difference_update(set(str2.split()))
    return set1


# -----------------------------------------------------------------------------
# 5
# Языки
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках
# - список таких языков.
import copy


def languages(stroka):
    list_str = stroka.split("\n")
    lst_pupil = []
    n_str = -2
    for s_str in list_str:
        s_str = s_str.strip()
        if n_str == -2:
            n_str = -1
        elif s_str.isdigit():
            n_str += 1
            lst_pupil.append(set())
        elif s_str:
            lst_pupil[n_str].add(s_str)

    lst2_pupil = copy.deepcopy(lst_pupil)
    all_pupil = lst_pupil.pop(0)
    all_pupil.intersection_update(*lst_pupil)
    print(len(all_pupil))
    print(all_pupil)
    one_pupil = lst2_pupil.pop(0)
    for lst in lst2_pupil:
        one_pupil.symmetric_difference_update(lst)
    print(len(one_pupil))
    print(one_pupil)


# -----------------------------------------------------------------------------
# 6
# Слова
# Во входной строке записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
def words(stroka):
    return len(stroka.replace("\n", ' ').split())


# -----------------------------------------------------------------------------
# 7
# Оглянемся назад
# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
def evklid(d1, d2):
    d1, d2 = max(d1, d2), min(d1, d2)
    while d1 != d2 and d2 != 0:
        d1, d2 = d2, d1 % d2
    return d1


# -----------------------------------------------------------------------------
# 8


# 1 --------------------------------------------------------------------------
print(dict_comprehensions())

# 2 --------------------------------------------------------------------------
stroka = """2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa      
3
Odessa
Moscow
Novgorod
"""
cities(stroka)

# 3 --------------------------------------------------------------------------
print(two_list("1 7 2 5 7", "1 7 4 6 2"))

# 4 --------------------------------------------------------------------------
print(count_different("1 7 2 5 7", "1 7 4 6 2"))

# 5 --------------------------------------------------------------------------
stroka = """3          
2    
Russian
English
3
Russian
Belarusian
English
3
Russian
Italian
French
"""
languages(stroka)

# 6
print(words(stroka))

# 7
print(evklid(19, 17))
