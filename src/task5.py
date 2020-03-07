# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N
# чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник


def inp(n):
    lang_list_one = []
    for lang in range(n):
        string = input('Enter ')
        lang_list_one.append(string)
    return set(lang_list_one)


lang_of_all = []
numb_of_stud = int(input("Enter number of students "))
for i in range(numb_of_stud):
    k = int(input('Number of languages of studend '))
    lang_of_all.append(inp(k))
all_stud_know = set()
one_stud_know = lang_of_all[0]
for el in lang_of_all:
    all_stud_know.update(el)
    one_stud_know = one_stud_know.intersection(el)
print('All students knows {} languages'.format(len(all_stud_know)))
print(list(all_stud_know))
print('At liest one student knows {} language'.format(len(one_stud_know)))
print(list(one_stud_know))
