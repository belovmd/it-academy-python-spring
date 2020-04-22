"""В файле хранятся данные с сайта IMDB.

Скопированные данные хранятся в файле ./data5/ratings.list.

Откройте и прочитайте файл(если его нет необходимо вывести ошибку).

Найдите ТОП250 фильмов и извлеките заголовки.

Программа создает 3 файла: top250_movies.txt – названия фильмов,

ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""

from collections import Counter

START_LINE = 29

file_path = './data5/ratings.list'
top_movies_path = 'top250_movies.txt'
years_path = 'years.txt'
ratings_path = 'ratings.txt'

movies_years = list()
movies_ratings = list()
quantity_years = dict()
quantity_ratings = dict()


def document_parser():
    counter = 1
    try:
        with open(file_path, 'r', ) as file:
            top_movies_file = open(top_movies_path, 'w')
            for line in file:
                if counter >= START_LINE:
                    all_data, year = line.split('(')
                    distribution, votes, ranting, *title \
                        = all_data.strip().split('  ')
                    movies_years.append(year[:4])
                    movies_ratings.append(ranting.strip())
                    top_movies_file.write(*title)
                    top_movies_file.write('\n')
                if counter == 250:
                    break
                counter += 1
            top_movies_file.close()
        year_histogram()
        rating_histogram()
        print('Success')
    except FileNotFoundError:
        print('File not found')


def year_histogram():
    quantity_years.update(Counter(movies_years))
    with open(years_path, 'w') as file_years:
        for year, quantity in quantity_years.items():
            histogram = ' *' * quantity
            result = str(year) + ': ' + str(quantity) + histogram + '\n'
            file_years.write(result)


def rating_histogram():
    quantity_ratings.update(Counter(movies_ratings))
    with open(ratings_path, 'w') as file_ratings:
        for rating, quantity in quantity_ratings.items():
            histogram = ' *' * quantity
            result = str(rating) + ': ' + str(quantity) + histogram + '\n'
            file_ratings.write(result)


if __name__ == '__main__':
    document_parser()
