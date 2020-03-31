# Дан список стран и городов каждой страны. Затем даны названия городов.
#  Для каждого города укажите, в какой стране он находится.

d = {}
for i in range(int(input("введите количество стран"))):
    country, *city = input("введите название страны, затем названия городов ").split()  # * - объединение элементов
    d[country] = city
list2 = []
for j in range(int(input("введите колличество городов"))):
    city = input("введите название городов")
    list2.append(city)
    for key, value in d.items():
        if list2[j] in value:
            print(key)
