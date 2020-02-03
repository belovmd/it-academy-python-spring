def mult_two(a, b):
    return a * b


def say_hi(name: str, age: int) -> str:
    name = "Alex"
    age = 32
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"


def easy_unpack(elements):
    return elements[0], elements[2], elements[-2]


def index_power(array: list, n: int):
    if len(array) <= n:
        return -1
    else:
        return array[n] ** n
