"""Города
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого
города укажите, в какой стране он находится.
=Входные данные
Программа получает на вход количество
стран N. Далее идет N строк, каждая строка
начинается с названия страны, затем идут
названия городов этой страны. В следующей
строке записано число M, далее идут M
запросов — названия каких-то M городов,
перечисленных выше.
=Выходные данные
Для каждого из запроса выведите название
страны, в котором находится данный город.
=Примеры
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

number_of_states = int(input("Insert number of states: "))
incoming_data_dict = {}
for _ in range(number_of_states):
    state_and_cities = str(input("Insert state and cities in this state: "))
    state_and_cities = state_and_cities.split()
    state_and_cities = {element: state_and_cities[0]
                        for element in state_and_cities[1:]}
    for element in incoming_data_dict:
        if element in state_and_cities:
            incoming_data_dict[element] += (', ' + state_and_cities[element])
            state_and_cities = {
                key: state_and_cities[key]
                for key in state_and_cities.keys() - {element}}
    incoming_data_dict.update(state_and_cities)

number_of_cities = int(input("Insert number of cities: "))
incoming_cities = []
for _ in range(number_of_cities):
    city = str(input("Insert name of the city: "))
    incoming_cities.append(city)

for cities in incoming_cities:
    for city, country in incoming_data_dict.items():
        if cities == city:
            print(country)
