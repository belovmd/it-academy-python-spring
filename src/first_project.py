"""Оформите решение задач из прошлых домашних работ в функции.

Напишите функцию runner. (все проще когда мы изучим модули, getattr и setattr)

runner() – все фукнции вызываются по очереди

runner(‘func_name’) – вызывается только функцию func_name.

runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""

import tasks_module


def runner(*args):
    function = []
    [function.append(elem) for elem in dir(tasks_module) if elem[:2] != '__']
    if args:
        for elem in args:
            print(getattr(tasks_module, elem))
    else:
        for elem in function:
            print(getattr(tasks_module, elem))


runner()
runner('swap_numbers')
runner('remove_duplicate_characters', 'swap_numbers', 'fibonacci')
