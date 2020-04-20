# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
# runner. (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
import functions


def runner(*names):
    func_list = [getattr(functions, el) for el in dir(functions) if
                 callable(getattr(functions, el))]
    if names:
        for el in names:
            if hasattr(functions, str(el)) and getattr(functions,
                                                       el) in func_list:
                try:
                    getattr(functions, el)()
                except TypeError:
                    print('Function {} has no args'.format(el))
    else:
        print('Enter function!')


runner('nod')
runner()
runner(5)
runner('nod', 'quantity', 'different_words')
