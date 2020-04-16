"""Каждый из N школьников некоторой школы
знает Mi языков. Определите, какие языки
знают все школьники и языки, которые
знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит
количество школьников N. Далее идет N
чисел Mi, после каждого из чисел идет Mi
строк, содержащих названия языков, которые
знает i-й школьник.
Пример:
3  - N количество школьников
2  - M1 количество языков первого школьника
Russian    - языки первого школьника
English
3  - M2 количество языков второго школьника
Russian
Belorussian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков,
которые знают все школьники. Начиная со второй
строки - список таких языков. Затем - количество
языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

number = int(input("Insert the number of students: "))
data_list = []
data_list_separated = []
data_set_separated = []

for element in range(number):
    data_list_separated.append([])
    number_of_languages = int(input(
        "Insert the number of languages for student "
        "№{number}: ".format(number=(element + 1))))

    for languages_element in range(number_of_languages):
        lang = str(input(
            "Insert the language "
            "№{numb}: ".format(numb=(languages_element + 1))))
        data_list.append(lang)
        data_list_separated[element].append(lang)

set_all_languages = set(data_list)

for el in data_list_separated:
    el = set(el)
    data_set_separated.append(el)

for numb in range(1, len(data_set_separated)):
    data_set_separated[0].intersection_update(data_set_separated[numb])

print("The number of languages known to everyone: ", len(data_set_separated[0]))
print("Languages known to everyone: ", end='')
for languages in data_set_separated[0]:
    print(languages, end=' ')

print("\nNumber of all unique languages:", len(set_all_languages))
print("All unique languages:", end=' ')
for lang in set_all_languages:
    print(lang, end=' ')
