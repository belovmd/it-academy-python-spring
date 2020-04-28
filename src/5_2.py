"""Создайте декоратор, который хранит
результаты вызовы функции (за все время
вызовов, не только текущий запуск программы)
"""


from datetime import datetime
from os import path

if path.exists('defs_results.txt'):
    pass
else:
    f = open('defs_results.txt', 'w')
    f.close()


def dec(func):
    def wrapper(*args, **kwargs):
        call_result = func(*args, **kwargs)
        with open('defs_results.txt', 'a') as ff:
            ff.write('Name: %s; Date: %s; Result: %s. \n'
                     % (func.__name__, datetime.now(tz=None), call_result))

        return call_result

    return wrapper


@dec
def my_function_param(b, c):
    d = str(b + c)
    return d


my_function_param(1, 2)
