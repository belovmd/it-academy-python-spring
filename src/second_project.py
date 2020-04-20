"""Дан список стран и городов каждой страны. Затем даны названия городов.

Для каждого города укажите, в какой стране он находится.

"""

countries = dict()
city = list()
for element in range(int(input("Enter quantity countries: "))):
    country_and_cities = (input("Enter country and cities: ").split())
    for elem in country_and_cities[1:]:
        countries.update({elem: country_and_cities[0]})
for element in range(int(input("Enter quantity cities: "))):
    city.append(input("Enter city: "))
for element in city:
    print(countries.get(element))
