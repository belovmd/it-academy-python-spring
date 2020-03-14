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
countries = dict()
for num in range(cnt_countries):
    line = input(f'Enter country name #{num} with its cities:').split()
    countries[line[0]] = set(line[1:])
cnt_queries = int(input('Enter count of queries:'))
queries = list()
for num in range(cnt_queries):
    queries.append(input(f'Enter query #{num} for city:'))
for city in queries:
    city_in_countries = [
        country for country, cities in countries.items() if city in cities]
    if city_in_countries:
        print(f'{city} city is in', *city_in_countries)
    else:
        print(f'{city} city did not find in any countries!!!')
