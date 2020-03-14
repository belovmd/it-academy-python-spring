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

for element in range(number):
    number_of_languages = \
        int(input("Insert the number of languages for student "
                  "№{number}: ".format(number=(element + 1))))

    for languages_element in range(number_of_languages):
        data_list.append(str(input(
            "Insert the language "
            "№{numb}: ".format(numb=(languages_element + 1)))))

print(data_list)

dct_all_languages = \
    {languages: data_list.count(languages) for languages in data_list}

print(dct_all_languages)

print("The number of languages known to everyone: ", end='')
know_to_everyone = 0
for lang in dct_all_languages:
    if dct_all_languages[lang] == number:
        know_to_everyone += 1
print(know_to_everyone, "\nLanguages known to everyone: ", end='')
for lang in dct_all_languages:
    if dct_all_languages[lang] == number:
        print(lang, end=' ')
print("\nNumber of all unique languages:",
      len(dct_all_languages), "\nAll unique languages: ", end='')
for lang in dct_all_languages:
    print(lang, end=' ')
