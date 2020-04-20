import datetime
import functools


def counter_calls_single_file(func):
    """Decorator for function calls counting

    Create 'function_name'_counter.txt in current directory
    with number of decorated function calls
    """

    try:
        with open('{}_counter.txt'.format(func.__name__), 'r') as file:
            name, counter = file.readline().split(': ')
    except FileNotFoundError:
        counter = 0
    except Exception:
        print('Error with Open/Close {}_counter file'.format(func.__name__))
        return func

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        nonlocal counter
        call_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        counter = int(counter) + 1

        with open('{}_counter.txt'.format(func.__name__), 'w') as file:
            file.write(
                '{}: {}\nlast function call time: {}'.format(
                    func.__name__, str(counter), call_time))

        return result
    return wrapper


def counter_calls_common_file(func):
    """Decorator for function calls counting

    Create counter_common.txt in current directory
    with list of number of decorated functions calls
    """

    data_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        nonlocal data_dict
        call_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        func_name = func.__name__

        try:
            with open('counter_common.txt', 'r') as file:

                for line in file.readlines():
                    name_value, last_call_time = line.strip().split(
                        ' last function call: ')
                    name, value = name_value.split(' calls: ')
                    data_dict[name] = [value, last_call_time]

                data_dict.setdefault(func_name, [0, call_time])

        except FileNotFoundError:
            data_dict.setdefault(func_name, [0, call_time])

        except Exception:
            print(
                'Error with Open/Close counter_common.txt'
            )
            return result

        data_dict[func_name][0] = int(data_dict.get(func_name)[0]) + 1
        data_dict[func_name][1] = call_time

        with open('counter_common.txt', 'w') as file:
            for name, calls in data_dict.items():
                file.writelines(
                    '{} calls: {} last function call: {}\n'.format(
                        name, str(calls[0]), calls[1]))

        return result
    return wrapper


@counter_calls_common_file
@counter_calls_single_file
def foo_1(*args, **kwargs):
    """Simple function for decorator test"""
    return 1


@counter_calls_common_file
@counter_calls_single_file
def foo_2(*args, **kwargs):
    """Simple function for decorator test"""
    return 2


@counter_calls_common_file
@counter_calls_single_file
def foo_3(*args, **kwargs):
    """Simple function for decorator test"""
    return 3


@counter_calls_common_file
@counter_calls_single_file
def foo_4(*args, **kwargs):
    """Simple function for decorator test"""
    return 4


foo_1(1, 5, d=6)
foo_1()
foo_2(d=8, g='f')
foo_3()
foo_3('1', 5)
foo_3()
foo_4()
foo_4()
