import test_func_1
import test_func_2
import test_func_3
from types import FunctionType

all_modules = [test_func_1, test_func_2, test_func_3]


def runner(*args):
    """Runner of callable objects without arguments

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
        if isinstance(obj, FunctionType) and attr_in_query:
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
        if type(obj).__name__ == 'module'
    ]

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
