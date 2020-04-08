# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N
# чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник
N = int(input('Enter number of students '))
students = []
for _ in range(N):
    languages = input().split()
    students.append(set(languages))
one_student = students[0].intersection(*students[1:])
all_student = students[0].union(*students[1:])
print('All students knows {} languages'.format(all_student))
print('At least one student knows {} languages'.format(one_student))
