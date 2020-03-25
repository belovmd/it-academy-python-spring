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
