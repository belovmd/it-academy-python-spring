import pack1.tasks4 as tasks

# 1 --------------------------------------------------------------------------
# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
dict_func_param = {
    'cities':
        """2
        Russia Moscow Petersburg Novgorod Kaluga
        Ukraine Kiev Donetsk Odessa
        3
        Odessa
        Moscow
        Novgorod
        """,
    'two_list':
        "1 7 2 5 7,1 7 4 6 2",
    "count_different":
        "1 7 2 5 7,1 7 4 6 2",
    'languages':
        """3
        2
        Russian
        English
        3
        Russian
        Belarusian
        English
        3
        Russian
        Italian
        French
        """,
    'words':
        """3
        2
        Russian
        English
        3
        Russian
        Belarusian
        English
        3
        Russian
        Italian
        French
        """,
}


def runner(*args):
    if not args:
        args = []
        glob_args = dir(tasks)
        for arg in glob_args:
            if callable(getattr(tasks, arg)) and not arg.startswith("__"):
                args.append(arg)
    print(args)
    for arg in args:
        if arg in dict_func_param:
            getattr(tasks, arg)(dict_func_param.get(arg))
        else:
            getattr(tasks, arg)()


runner()
runner('count_different')
runner('words', 'cities')
