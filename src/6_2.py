"""Создайте декоратор, который вызывает
задекорированную функцию пока она не
выполнится без исключений (но не более
n раз - параметр декоратора). Если превышено
количество попыток, должно быть возбуждено
исключение типа TooManyErrors"""


import random


def run_func_n_times(n):
    def decorator_of_func(func):

        def wrapper():
            i = 0
            while True:
                i += 1
                print("This is run number %s" % i)
                pre_res = random.uniform(0.8, 1.5)
                result = func(pre_res)
                if pre_res <= 1:
                    print("Correct pre_res")
                    break
                if i == n:
                    raise Exception("TooManyErrors")

        return wrapper

    return decorator_of_func


@run_func_n_times(5)
def something(divisor_part):
    try:
        if divisor_part > 1:
            raise ZeroDivisionError
        else:
            res = 1 / int(2 - divisor_part)
            print(int(res))
            print("NICE ONE!")
    except ZeroDivisionError:
        print("Random Number Generator Error")


something()
