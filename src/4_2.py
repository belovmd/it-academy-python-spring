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


number_of_states = \
    int(input("Insert number of states: "))
incoming_data_list = []
for element in range(number_of_states):
    state_and_cities = str(input("Insert state and cities in this state: "))
    state_and_cities = state_and_cities.split()
    incoming_data_list.append(state_and_cities)

number_of_cities = \
    int(input("Insert number of cities: "))
incoming_cities = []
for element in range(number_of_cities):
    city = str(input("Insert name of the city: "))
    incoming_cities.append(city)

for cities in incoming_cities:
    for element in incoming_data_list:
        if cities in element:
            print(element[0], end=' ')
    print("\r")

