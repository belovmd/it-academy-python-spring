"""4 - films rating parser

В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""
from collections import Counter
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d %(message)s",
)
logger = logging.getLogger(__name__)


def get_file_handler(file_path: str):
    try:
        return open(file_path, "r", encoding="ISO-8859-1")
    except FileNotFoundError as ex:
        logger.warning(f"File not found: {ex}")
        return None


def save_to_file(filename, data):
    with open(filename, 'w', encoding="UTF-8") as file_handler:
        file_handler.write('\n'.join(data))


def parser(file_path, begin_with=28):
    """parser function:

    Parse text file with film ratings and save results into another files:
        - top250_movies.txt
        - ratings.txt
        - years.txt
    """

    film_names = []
    ratings = []
    years = []

    file_handler = get_file_handler(file_path)
    if file_handler is not None:
        with file_handler:
            for ind, line in enumerate(file_handler):
                try:
                    if ind < begin_with:
                        continue
                    distr, votes, rank, title_year = line.strip().split('  ')
                    title, year = title_year.strip('() ').split(' (')
                    film_names.append(title)
                    rating = rank.strip()
                    ratings.append(rating)
                    years.append(year)
                    if len(film_names) == 250:
                        break
                except Exception as ex:
                    logger.warning(f"Error parse data: {ex}")
                    break
        ranks_gist = [f'{r} - {c}' for r, c in Counter(ratings).most_common()]
        years_gist = [f'{y} - {c}' for y, c in Counter(years).most_common()]
        save_to_file('top250_movies.txt', film_names)
        save_to_file('ratings.txt', ranks_gist)
        save_to_file('years.txt', years_gist)


if __name__ == "__main__":
    parser('data5/ratings.list')
