""" Школьники и языки

Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет
N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.
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
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя  бы один школьник, на следующих
строках - список таких языков.
"""


journal = {}
languages = set()
print('Input N - pupils number:')
n = int(input())
for i in range(n):
    print('Input number of languages for pupil #{}:'.format(i + 1))
    m = int(input())
    pupils_languages = set()
    for _ in range(m):
        language = input()
        pupils_languages.add(language)
        languages.add(language)
    journal[i] = pupils_languages


popular_languages = []
non_popular_languages = []

for language in languages:
    is_everybody_knows = True
    is_at_least_one_knows = False
    for lang_list in journal.values():
        if language in lang_list:
            is_at_least_one_knows = True
        else:
            is_everybody_knows = False
    if is_everybody_knows:
        popular_languages.append(language)
    if is_at_least_one_knows:
        non_popular_languages.append(language)

print(len(popular_languages))
for language in popular_languages:
    print(language)
print(len(non_popular_languages))
for language in non_popular_languages:
    print(language)