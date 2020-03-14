"""Задача 5 - Какие языки знают школьники?

Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

"""
from functools import reduce


def wich_langs_know():
    cnt_students = int(input('Enter count of students:'))
    students_langs = dict()
    for student in range(cnt_students):
        cnt_langs = int(input(
            f'Enter count of languages the student #{student + 1} knows:'))
        langs = list()
        for lang in range(cnt_langs):
            langs.append(
                input(f'Student #{student + 1} knows language #{lang + 1}:'))
        students_langs[student] = langs
    lang_know_all = list(
        reduce((lambda s1, s2: s1 & s2), map(set, students_langs.values())))
    lang_know_at_least_one = list(
        reduce((lambda s1, s2: s1 | s2), map(set, students_langs.values())))

    if lang_know_all:
        print('Languages ​​that all students know:', *lang_know_all)
    else:
        print('There are no languages ​​that all students know')

    if lang_know_at_least_one:
        print('Languages that know at least one student:',
              *lang_know_at_least_one)
    else:
        print('Students do not know a any languages')


if __name__ == '__main__':
    wich_langs_know()
