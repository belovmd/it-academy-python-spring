"""Создайте декоратор, который хранит результаты вызовы функции

(за все время вызовов, не только текущий запуск программы)

"""

import os


def dec(function):
    numbers = 0

    def wrapper():
        nonlocal numbers
        numbers += function()
        return numbers

    return wrapper


@dec
def func():
    return 1


if os.path.exists('text.txt'):
    with open('text.txt', 'a') as file:
        for elem in range(3):
            file.write(str(func()))
            file.write('\n')
    print("File added success")
else:
    try:
        with open('text.txt', 'w') as file:
            file.write('start\n')
            print("File created success")
    except FileNotFoundError:
        print('File not found')
