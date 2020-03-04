""" 2. Города
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""

dict_countries = {}
for item in range(int(input("Введите количество стран: "))):
    lst = input("Введите страну и города: ").split()
    dict_countries.update({lst[0]: {item for item in lst[1:]}})
lst = []
for item in range(int(input("Введите количество городов: "))):
    cities = input("Введите города: ")
    for key in dict_countries.keys():
        if cities in dict_countries[key]:
            lst.append(key)
print(lst)
