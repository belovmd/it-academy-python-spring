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
lst_of_countries = {}
N = int(input("Enter number of countries "))
for _ in range(N):
    country, *cities = input().split()
    for el in cities:
        lst_of_countries[el] = lst_of_countries.get(el, '') + country + ' '
print('Enter M and cities')
M, *lst_of_cities = input().split()
for el in lst_of_cities:
    print(el, lst_of_countries.get(el))
