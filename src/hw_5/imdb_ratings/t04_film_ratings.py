""" Film ratings

Read film ratings data from a file: ./data5/ ratings.list.

If a file does not exist raise an error message.
Find top 250 movies and its titles. Program should create 3 files:
    top250_movies.txt – titles,
    ratings.txt – ratings bar chart,
    years.txt – years bar chart.
"""


import datetime
import re


FILE_PATH = 'data5/ratings.list'
FIRST_YEAR = 1895
MAX_RATING = 10
MIN_RATING = 0
NUMBER_OF_COMMENT_LINES = 28
RATINGS_FILE_PATH = 'ratings.txt'
TITLES_FILE_PATH = 'top250_movies.txt'
TOP_FILES_NUMBER = 250
YEARS_FILE_PATH = 'years.txt'


def get_film_year(film_title):
    pattern = r'\d{4}'
    result = re.findall(pattern, film_title)
    return result[-1] if result else ''


def get_top_250_movies(file_path=FILE_PATH):
    try:
        file = open(file_path, 'r')
    except IOError as e:
        print('Unable to open the file {}'.format(FILE_PATH), e)
    else:
        # create years dict
        current_year = datetime.datetime.now().year
        years = {str(year): 0
                 for year in range(FIRST_YEAR, current_year + 1)}
        years[''] = 0

        # create ratings dict
        ratings = {str(round(i + j * 0.1, 2)): 0
                   for i in range(MIN_RATING, MAX_RATING)
                   for j in range(MIN_RATING, MAX_RATING)}
        ratings[str(MAX_RATING)] = 0

        titles = []
        file_count = 0

        with file:
            # skip comments in the first lines
            for _ in range(NUMBER_OF_COMMENT_LINES):
                next(file)

            # read film data
            for line in file:
                if file_count >= TOP_FILES_NUMBER:
                    break

                _, _, rank, *film_data = line.split()

                title = ' '.join(film_data)
                titles.append(title)
                year = get_film_year(title)
                years[year] += 1
                ratings[rank] += 1
                file_count += 1

        create_ratings_bar_chart(ratings)
        create_years_bar_chart(years)
        create_top_250_movies(titles)


def create_years_bar_chart(years_dct: dict):
    write_non_zero_dict_to_file(years_dct, YEARS_FILE_PATH, int)


def create_ratings_bar_chart(ratings_dct: dict):
    write_non_zero_dict_to_file(ratings_dct, RATINGS_FILE_PATH, float)


def write_non_zero_dict_to_file(dct: dict, file_path: str, key_type):
    with open(file_path, 'w') as f:
        non_zero_dict = {key_type(key): value
                         for key, value in dct.items()
                         if value}
        print(non_zero_dict, file=f)


def create_top_250_movies(titles: list):
    with open(TITLES_FILE_PATH, 'w') as f:
        for title in titles:
            f.write(title + '\n')


if __name__ == '__main__':
    get_top_250_movies()
