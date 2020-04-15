"""Задача 2 - Города

Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то
M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный
город.

"""
cnt_countries = int(input('Enter count of countries:'))
cities_dict = dict()
for num in range(cnt_countries):
    line = input(f'#{num}: Enter country name with its cities:').split()
    country = line[0]
    cities = line[1:]
    cities_dict.update({
        city: cities_dict.get(city, []) + [country] for city in cities
    })

cnt, *queries = input('Enter count of queries and cities inline:').split()

for city in queries:
    city_in_countries = cities_dict.get(city, None)
    if city_in_countries is not None:
        print(f'{city} city is in', end=' ')
        print(*city_in_countries, sep=', ', end='\n')
    else:
        print(f'{city} city did not find in any countries!!!')
