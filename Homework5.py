"""
1.
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""


def dict_compregensions():
    dict = {(el): el ** 3 for el in range(1, 20)}
    print(dict)


def coutrys_and_city():
    # Дан список стран и городов каждой страны. Затем даны названия городов.
    # Для каждого города укажите, в какой стране он находится.
    # Входные данные
    # Программа получает на вход количество стран N.
    # Далее идет N строк, каждая строка начинается с названия страны,
    # затем идут названия городов этой страны.
    # В следующей строке записано число M, далее идут M запросов — названия
    # каких-то M городов, перечисленных выше.

    dict = {}
    for i in range(int(input())):
        country, *cities = input().split()
        for city in cities:
            dict[city] = country

    for i in range(int(input())):
        print(dict[input()])


def words():
    # Во входной строке записан текст.
    # Словом считается последовательность непробельных символов идущих подряд,
    # слова разделены одним или большим числом пробелов или символами конца строки.
    # Определите, сколько различных слов содержится в этом тексте.


    s = "Its character set is continued in the following Unicode block"

    words = 0
    prev = True

    for ch in s:
        cur = str.isspace(ch)
        if prev and not cur: words += 1
        prev = cur

    print(words)


def runner(*name):