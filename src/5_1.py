"""Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только
функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все
переданные функции """


import HomeWorks

def runner(*func):
    for element in func:
        getattr(dir(HomeWorks), element, "Task is not chosen")()

    if not func:
        for element in HomeWorks.__dict__:
            attr = ['__module__', '__dict__',
                    '__weakref__', '__doc__']
            if str(element) not in attr:
                getattr(HomeWorks(), element, "Task is not chosen")()


runner()
