""" 5. Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример:
3          - N количество школьников
2          - M1 количество языков первого школьника
Russian    - языки первого школьника
English
3          - M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают
все школьники. Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

student_languages = {}
languages_set = set()
for student in range(int(input("Введите количество учеников: "))):
    language_lst = []
    for _ in range(int(input("Введите количество языков: "))):
        language_lst.append(input
                            ("Введите языки которые знает ученик: "))
    student_languages.update({student:
                             {elem for elem in language_lst}})
    languages_set.update({elem for elem in language_lst})
languages = list(languages_set)
for values in student_languages.values():
    languages_set = languages_set.intersection(values)
print("Количество языков которые знают школьники:", len(languages))
print("Языки которые знают школьники:", *languages)
print("Количество языков которые знает хотя бы один школьник:",
      len(languages_set))
print("Языки которые знает хотя бы один школьник:", *languages_set)
