"""Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только
функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все
переданные функции """

from src import homeworks

parameters = {"hi_name": ["Ivan", "Ivanov"]}


def runner(*func):
    db = []
    [db.append(element) for element in dir(homeworks) if element[:2] != "__"]

    try:
        for element in func:
            callable(getattr(homeworks, element)(parameters.get(element)))

        if not func:
            for element in db:
                callable(getattr(homeworks, element)(parameters.get(element)))

    except AttributeError:
        print("Attribute Error")
    except TypeError:
        print("Type Error")


no_function = None

runner()
runner('hello_world', 'iterable_friends')
runner('no_function')
runner(no_function)
