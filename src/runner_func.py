# please uncomment all imports

# import test_func_1 as file1
# from test_func_1 import func3
# import test_func_2 as file2
# import test_func_3


def runner(*args):
    """Runner of callable objects without arguments

    Try to call all callable objects from all importing objects or
    all callable objects with names from args in all importing objects
    Add condition type(obj).__name__ == 'function' before 'try'
    if need just function calls.

    In case of necessary arguments for callable objects
    error message will print

    :param args: list of names of callable objects
    :return: None
    """
    def call(obj, attr):
        """Function for calling objects

        :param obj: object to call
        :param attr: name of attribute
        :return: None
        """
        attr_in_query = attr in args or not args
        if callable(obj) and not attr.startswith('__') and attr_in_query:
            try:
                obj()
            except TypeError as error:
                print(
                    '!!!! {} from {} call '
                    'error: {}'.format(obj.__name__, obj.__module__, error)
                )
            except Exception:
                print(
                    '!!!! {} from {} call '
                    'error'.format(obj.__name__, obj.__module__)
                )

    all_attrs = globals()

    list_of_modules = [
        obj for attr, obj in all_attrs.items()
        if type(obj).__name__ == 'module' and not attr.startswith('__')
    ]

    args = set(args)

    for module in list_of_modules:
        for attr in module.__dir__():
            obj = getattr(module, attr)
            call(obj, attr)

    for attr, obj in all_attrs.items():
        if attr != 'runner':
            call(obj, attr)


runner()
runner('func5', 'func1')
runner('func3')
runner('func7')
