""" Decorator task

Create a decorator that stores results of all function calls (take into account
all script executions).
"""


from os import path
import random


COLORS_LIST = ['red', 'green', 'blue', 'yellow', 'white']
DICT_SEPARATOR = ':'
ELEMENTS_SEPARATOR = ','
END_OF_LINE = '\n'
FILE_NAME = 'calls.txt'
RANDOM_RANGE = 100


def set_call_result(f_name, f_result):
    lines = []
    function_found = False
    if path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for line in f:
                function_name, results = line.split(DICT_SEPARATOR)
                if not function_found and function_name == f_name:
                    results = (results[:-1] +
                               ELEMENTS_SEPARATOR +
                               str(f_result) +
                               END_OF_LINE)
                    function_found = True
                lines.append(function_name + DICT_SEPARATOR + results)

    if not function_found:
        lines.append(f_name + DICT_SEPARATOR + str(f_result) + END_OF_LINE)

    with open(FILE_NAME, 'w') as f:
        f.writelines(lines)


def call_count(decorated_function):
    def call_count_wrapper(*args, **kwargs):
        result = decorated_function(*args, **kwargs)
        set_call_result(decorated_function.__name__, result)
        return result
    return call_count_wrapper


@call_count
def get_random_number():
    return random.randint(0, RANDOM_RANGE)


@call_count
def get_random_color():
    return random.choice(COLORS_LIST)


if __name__ == '__main__':
    get_random_number()
    get_random_number()
    get_random_color()
    get_random_color()
    get_random_number()
    get_random_color()
