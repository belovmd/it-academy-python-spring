"""Дан список стран и городов каждой страны. Затем даны названия городов.

Для каждого города укажите, в какой стране он находится.

"""

countries = {}
for element in range(int(input("Enter quantity countries: "))):
    words = input("Enter country and towns: ").split()
    countries.update({words[0]: {elem for elem in words[1:]}})
for element in range(int(input("Enter quantity towns: "))):
    town = (input("Enter town: "))
    for key in countries.keys():
        if town in countries[key]:
            print(key)
