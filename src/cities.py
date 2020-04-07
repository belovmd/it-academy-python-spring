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

dict_cities = {}
for _ in range(int(input("Введите количество стран: "))):
    country, *cities = input("Введите страну и города: ").split()
    for city in cities:
        dict_cities[city] = dict_cities.get(city, []) + [country]
lst_countries = []
for _ in range(int(input("Введите количество городов: "))):
    city = input("Введите название города: ")
    if city in dict_cities.keys():
        print(dict_cities[city])
