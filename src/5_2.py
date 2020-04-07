"""Создайте декоратор, который хранит
результаты вызовы функции (за все время
вызовов, не только текущий запуск программы)
"""


from os import path
import time

if path.exists('defs_results.txt'):
    pass
else:
    f = open('defs_results.txt', 'w')
    f.close()


def dec(func):
    def wrapper():
        with open('defs_results.txt', 'a') as ff:
            ff.write(func() + '\n')
        return func()
    return wrapper


@dec
def my_function():
    a = time.ctime()
    return a


print(my_function())
