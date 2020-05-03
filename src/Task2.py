"""Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметрдекоратора). Если превышено количество
попыток, должно быть возбуждено исключение типа TooManyErrors
"""

import random


class TooManyErrors(Exception):
    def __init__(self):
        print("Error: TooManyErrors")
        raise SystemExit


def retry(max_try):
    def dec(call_error):
        def wrapper(*args, **kwargs):
            for elem in range(1, max_try + 1):
                try:
                    return call_error(*args, **kwargs)
                except ImportError:
                    if elem == max_try:
                        raise TooManyErrors
        return wrapper
    return dec


@retry(max_try=5)
def call_error():
    a = random.randint(0, 10)
    if a:
        raise ImportError
    else:
        return "The function was completed successfully"


print(call_error())
