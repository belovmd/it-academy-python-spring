import ddt
from io import StringIO
import os
import re
import shutil
import sys
import task3 as test_module
import unittest

working_catalog = 'data5/'
# doc_parser() from test_module should work with working_catalog
# if doc_parser() works with current directory: working_catalog = './'

DIRECTORY = os.path.abspath(os.path.dirname(working_catalog))
RATING_LIST = os.path.join(DIRECTORY, 'ratings.list')
RATING_LIST_RENAME = os.path.join(DIRECTORY, 'ratings12345.list')
TOP250_MOVIES = os.path.join(DIRECTORY, 'top250_movies.txt')
RATINGS = os.path.join(DIRECTORY, 'ratings.txt')
YEARS = os.path.join(DIRECTORY, 'years.txt')


def file_handler(file_name):
    """Function to create list of strings from file

    :param file_name: existing filename
    :return: list of strings from file
    """
    with open(file_name) as file:
        return [line.strip() for line in file]


def gist_handler(file_name, expression):
    """Ratings gist file parser

    If we don't know format between rating and value
    we should use re.
    :param expression: expression for regex
    :param file_name: <directory>/ratings.txt
    :return: list of tuples
    """
    with open(file_name) as file:
        result = []
        for line in file:
            ratings = re.findall(expression, line)
            line = line.rstrip()
            symbol = line[-1]
            value = 0
            while symbol == line[-value - 1]:
                value += 1
            result.append((ratings, value))
        return result


@ddt.ddt
class IMDBParserTest(unittest.TestCase):

    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)
    os.remove(TOP250_MOVIES) if os.path.isfile(TOP250_MOVIES) else None
    os.remove(YEARS) if os.path.isfile(YEARS) else None
    os.remove(RATINGS) if os.path.isfile(RATINGS) else None
    shutil.copy('tests/files/ratings.list', RATING_LIST)
    test_module.doc_parser()

    def test_error_msg(self):
        old_file_name = RATING_LIST
        new_file_name = RATING_LIST_RENAME
        os.rename(old_file_name, new_file_name)

        saved_stdout = sys.stdout
        result = None

        try:
            sys.stdout = StringIO()
            test_module.doc_parser()
            result = sys.stdout.getvalue()
        finally:
            sys.stdout = saved_stdout

        self.assertIn('[Errno 2] No such file', result)

        os.rename(new_file_name, old_file_name)

    @ddt.data(
        (TOP250_MOVIES, True),
        (RATINGS, True),
        (YEARS, True),
    )
    @ddt.unpack
    def test_files_creation(self, file_name, expected):
        """File {} not exists"""
        self.assertEqual(os.path.isfile(file_name), expected)

    @unittest.skipIf(not os.path.isfile(TOP250_MOVIES), 'File not exists')
    def test_titles_file(self):
        result = file_handler(TOP250_MOVIES)
        expected = file_handler('tests/files/top250_movies.txt')
        self.assertCountEqual(result, expected, msg='Wrong data')

    @unittest.skipIf(not os.path.isfile(RATINGS), 'File not exists')
    def test_rating_gist(self):
        result = gist_handler(RATINGS, r'\d\.\d')
        expected = gist_handler('tests/files/ratings.txt', r'\d\.\d')
        self.assertCountEqual(result, expected, msg='Wrong data')

    @unittest.skipIf(not os.path.isfile(YEARS), 'File not exists')
    def test_years_gist(self):
        result = gist_handler(YEARS, r'\d{4}')
        expected = gist_handler('tests/files/years.txt', r'\d{4}')
        self.assertCountEqual(result, expected, msg='Wrong data')

    @ddt.data('1', {1: 1}, 1, [1])
    def test_type_error(self, data):
        with self.assertRaises(TypeError):
            test_module.doc_parser(data)
