# Создайте декоратор, который хранит результаты вызовы функции (за все время
# вызовов, не только текущий запуск программы)
import time


def dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        file = open('text.txt', 'a')
        file.write('Functions name: {}\nCalled: {}\nResult: {}\n\n'.format(
            func.__name__, time.asctime(), res))
        file.close()
        return res
    return wrapper


@dec
def numb(num):
    return num


@dec
def addition(a, b):
    return a + b


numb(8000)
addition(3, 3)
f = open('text.txt')
print(f.read())
f.close()
