"""Calculating with Functions.

This time we want to write calculations using functions and get the results.

Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

"""


def zero(func=None):
    return 0 if not func else func(0)


def one(func=None):
    return 1 if not func else func(1)


def two(func=None):
    return 2 if not func else func(2)


def three(func=None):
    return 3 if not func else func(3)


def four(func=None):
    return 4 if not func else func(4)


def five(func=None):
    return 5 if not func else func(5)


def six(func=None):
    return 6 if not func else func(6)


def seven(func=None):
    return 7 if not func else func(7)


def eight(func=None):
    return 8 if not func else func(8)


def nine(func=None):
    return 9 if not func else func(9)


def plus(b):
    return lambda a: a + b


def minus(b):
    return lambda a: a - b


def times(b):
    return lambda a: a * b


def divided_by(b):
    return lambda a: a / b


if __name__ == '__main__':
    assert one(minus(three())) == -2
    assert nine(times(five())) == 45
    assert eight(divided_by(two())) == 4
    assert four(plus(five(times(two())))) == 14
