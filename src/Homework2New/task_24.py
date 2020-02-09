# arithmetic tasks solution
# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner
# function represents the right operand
# Division should be integer division.
# For example, this should return 2, not 2.666666...:


def zero(func=None):
    return func(0) if func else 0


def one(func=None):
    return func(1) if func else 1


def two(func=None):
    return func(2) if func else 2


def three(func=None):
    return func(3) if func else 3


def four(func=None):
    return func(4) if func else 4


def five(func=None):
    return func(5) if func else 5


def six(func=None):
    return func(6) if func else 6


def seven(func=None):
    return func(7) if func else 7


def eight(func=None):
    return func(8) if func else 8


def nine(func=None):
    return func(9) if func else 9


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: x // num


if __name__ == '__main__':
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
