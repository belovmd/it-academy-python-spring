"""2 - Decorator count run function all time
Создайте декоратор, который хранит результаты вызовы функции (за все время
вызовов, не только текущий запуск программы)

"""

import json
import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d %(message)s",
)
logger = logging.getLogger(__name__)


def count_run(func):
    """Accumulate count of function runs, and save number in to file"""
    try:
        with open('count_run.json', 'r') as file_handler:
            data = file_handler.read()
            logger.info(f"Reading data from file: {data}")
            if data:
                count = json.loads(data)['count']
    except Exception as ex:
        logger.warning(f"Error reading file! Exception: {ex}")
        count = 0

    @wraps(func)
    def wrap(*args, **kwargs):
        """Wrapper function"""
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        try:
            with open('count_run.json', 'w') as file_handler:
                data = json.dumps({"count": count})
                file_handler.write(data)
        except Exception as ex:
            logger.warning(f"Error write data to file! Exception: {ex}")
        return {'result': result, 'count_runs': count}
    return wrap


@count_run
def simple_function(x, y):
    """Return sum of two elements x and y"""
    return x + y


if __name__ == '__main__':
    assert simple_function(1, 2) == {'result': 3, 'count_runs': 1}
    assert simple_function(3, 5) == {'result': 8, 'count_runs': 2}
    assert simple_function(2, 4) == {'result': 6, 'count_runs': 3}
