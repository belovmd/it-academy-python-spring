# 1.Dict comprehensions

dict = {(el): el ** 3 for el in range(1, 20)}
print(dict)

# 2. City

dict = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        dict[city] = country

for i in range(int(input())):
    print(dict[input()])

# 3 Даны два списка чисел.

"""Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""

list = set("123")
list2 = set("345")
print(len(list | list2))

# 4


# 5 Languages

stud = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, knownsomeone = set.inter(*stud), set.union(*stud)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(knownsomeone), *sorted(knownsomeone), sep='\n')

# 6 Words

"""Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

s = "Its character set is continued in the following Unicode block, " \
    "Phonetic Extensions Supplement."

words = 0
prev = True

for ch in s:
    cur = str.isspace(ch)

    if prev and not cur:
        words += 1

    prev = cur

print(words)

# 7 Back to the future

"""Даны два натуральных числа.Вычислите их наибольший
общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""

a = 30
b = 150

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)
