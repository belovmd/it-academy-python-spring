"""В файле хранятся данные с сайта
IMDB. Скопированные данные хранятся
в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его
нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките
заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

from os import path

if path.exists('./data5/ratings.list'):
    a = open('./data5/ratings.list', 'r')
    a.close()
else:
    print("The file doesn't exist")
    raise SystemExit

base_250 = []

with open('./data5/ratings.list', 'rt') as file:
    for index, line in enumerate(file):
        if 'The Shawshank Redemption' in line:
            start_250 = index
            break

with open('./data5/ratings.list', 'rt') as file:
    for index_2, line in enumerate(file):
        if start_250 <= index_2 <= (start_250 + 250):
            base_250.append(line)

list_ratings = []
list_years = []

with open('top250_movies.txt', 'w') as file:
    for element in range(len(base_250) - 1):
        base_250[element] = base_250[element].split('  ')

        list_ratings.append(base_250[element][5][-3:])

        base_250[element] = base_250[element][6]
        base_250[element] = base_250[element].split(' (')

        list_years.append(base_250[element][1][0:4])

        cinema_name = base_250[element][0]
        print(cinema_name)
        file.write(cinema_name + '\n')

list_ratings.sort()
list_years.sort()

dct_ratings = {element: list_ratings.count(element)
               for element in list_ratings}

dct_years = {element: list_years.count(element)
             for element in list_years}

with open('ratings.txt', 'w') as file:
    for element in dct_ratings:
        file.write(element + ' : '
                   + str(dct_ratings[element]) + '\n')

with open('years.txt', 'w') as file:
    for element in dct_years:
        file.write(element + ' : '
                   + str(dct_years[element]) + '\n')
