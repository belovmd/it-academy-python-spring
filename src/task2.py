# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные:
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия
# каких-то M городов, перечисленных выше.
# Выходные данные:
# Для каждого из запроса выведите название страны, в котором находится
# данный город.
N = int(input("Enter number of countries "))
countries = {}
for el in range(N):
    string = input('Enter country and cities ')
    countries.update({string[0]: string[1:]})

M = int(input("Enter number of cities "))
cities = []
for i in range(M):
    string = input('Enter cities ')
    cities.append(string)

while cities:
    for key in countries:
        if cities[0] in countries.get(key):
            print(key)
    cities = cities[1:]
