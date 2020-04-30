"""Создайте декоратор, который вызывает задекорированную функцию пока она

не выполнится без исключений (но не более n раз - параметр декоратора).

Если превышено количество попыток, должно быть возбуждено исключение

типа TooManyErrors

"""

from random import randint


def main_dec(number):
    def dec(function):
        def wrapper():
            quantity = 0
            while True:
                first_number = randint(0, 7)
                second_number = randint(0, 7)
                result = function(first_number, second_number)
                quantity += 1
                if result == 10:
                    break
                if quantity == number:
                    raise Exception('TooManyErrors')
        return wrapper
    return dec


@main_dec(7)
def addition(first_number, second_number):
    result = first_number + second_number
    try:
        if result != 10:
            raise ValueError
        else:
            print('Success!')
            return result
    except ValueError:
        print('Error!')


if __name__ == '__main__':
    addition()
