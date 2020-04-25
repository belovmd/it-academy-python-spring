"""2 - decorator
Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors

"""
import logging
from functools import wraps
import unittest

log_format = "%(asctime)s | %(levelname)s | " \
             "%(filename)s:%(lineno)d %(message)s"

logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


class TooManyErrors(Exception):
    def __init__(self, obj_name):
        super().__init__()
        self.obj_name = obj_name

    def __str__(self):
        return f'{self.obj_name} raise exception TooManyErrors'


def decor_runner(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(x, y):
            for time in range(n):
                func(x, y)
                y -= 1
                logger.info(f'{func.__name__} was running {time} times')
            else:
                logger.warning(f'Limit trying count. Counts = {time}')
                raise TooManyErrors(func.__name__)
            return func(x, y)
        return wrapper
    return decorator


@decor_runner(3)
def divide_numbers(x: int or float, y: int) -> float:
    try:
        result = x / y
        logger.info(f'divide_numbers({x}, {y}) => {result}')
    except ZeroDivisionError as ex:
        logger.warning(f'divide_numbers({x}, {y}): {ex}')
        raise ZeroDivisionError
    return result


class TestDecoratorRunFunction(unittest.TestCase):
    def test_exception_too_many_errors(self):
        logger.info('test__1')
        with self.assertRaises(TooManyErrors):
            divide_numbers(3, 5)

    def test_exception_zero_division(self):
        logger.info('test__2')
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(3, 2)


if __name__ == '__main__':
    unittest.main()
