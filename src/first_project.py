"""Оформите решение задач из прошлых домашних работ в функции.

Напишите функцию runner. (все проще когда мы изучим модули, getattr и setattr)

runner() – все фукнции вызываются по очереди

runner(‘func_name’) – вызывается только функцию func_name.

runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""

import tasks_module

params = {
    'swap_numbers': [1, 4, 0, 3, 6, 2, 0, 2],
    'fibonacci': 15,
    'remove_duplicate_characters': 'abc cde eft'
}


def runner(*args):
    function = []
    [function.append(elem) for elem in dir(tasks_module) if elem[:2] != '__']
    try:
        if args:
            for elem in args:
                callable(getattr(tasks_module, elem)(params.get(elem)))
        else:
            for elem in function:
                callable(getattr(tasks_module, elem)(params.get(elem)))
    except AttributeError:
        print('Attribute error')
    except TypeError:
        print('Type error')


if __name__ == '__main__':
    runner()
    runner('swap_numbers')
    runner('remove_duplicate_characters', 'swap_numbers', 'fibonacci')
    runner(1234)
    runner('12345')
