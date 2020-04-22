"""Создайте декоратор, который хранит результаты вызовы функции

(за все время вызовов, не только текущий запуск программы)

"""

from datetime import datetime

now = str()
now = datetime.now()


def dec(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        with open('text.txt', 'a') as file:
            file.write('function: {}\t datetime: {}\t result: {}\n'.format(
                function.__name__,
                now.strftime('%d-%m-%Y %H:%M'),
                result)
            )
        return result

    return wrapper


@dec
def power(number):
    return number ** 2


for i in range(1, 10):
    power(i)
