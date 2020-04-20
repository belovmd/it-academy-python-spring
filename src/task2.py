# Создайте декоратор, который вызывает задекорированную функцию пока она не
# выполнится без исключений (но не более n раз - параметр декоратора). Если
# превышено количество попыток, должно быть возбуждено исключение типа
# TooManyErrors
import random


def dec1(n):
    def dec(func):
        def wrapper():
            k = 0
            while True:
                res = func(random.randint(0, 10))
                k += 1
                if res == 3:
                    break
                if k == n:
                    raise Exception("TooManyErrors")
        return wrapper
    return dec


@dec1(10)
def function(e):
    try:
        if e != 3:
            raise ValueError("Wrong number!")
        else:
            print('Excellent!')
            return e
    except ValueError:
        print('Error!')


function()
