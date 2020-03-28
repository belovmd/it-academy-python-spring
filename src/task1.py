# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
# runner. (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
import func


def runner(*names):
    if names:
        [print(getattr(func, el)) for el in names]
    else:
        [print(getattr(func, el)) for el in dir(func)
         if el.startswith('__') is False]


runner('different_words')
runner('nod', 'different_words')
runner()
