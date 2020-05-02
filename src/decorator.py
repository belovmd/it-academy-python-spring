# 2 --------------------------------------------------------------------------
# Создайте декоратор, который вызывает задекорированную функцию пока она
# не выполнится без исключений (но не более n раз - параметр декоратора).
# Если превышено количество попыток, должно быть возбуждено исключение типа
# TooManyErrors


n_exception = 1000


class TooManyErrors(RuntimeError):
    def __init__(self, arg):
        self.args = [arg]


def decor(n_exept):
    def dec(func):
        def wrapper(*args, **kwargs):
            index = 0
            try:
                while True:
                    res = func(index)
                    if index > n_exept:
                        raise TooManyErrors("TooManyTimes")
                    index += 1
            except TooManyErrors as err:
                print(err, "number of attempts exceeded")
            except Exception as err:
                print(err)
            res = func(*args, **kwargs)
            return res

        return wrapper

    return dec


@decor(n_exception)
def fibonachi(n):
    f_prev = 0
    f_curr = 1
    for i in range(n - 1):
        f_prev, f_curr = f_curr, f_curr + f_prev
    return f_prev


print(fibonachi(21))
