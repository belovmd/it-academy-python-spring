""" Function runner

Implement a function runner that calls functions from hw_5.functions_to_run
package.
If a function was not imported no exception raises.
"""


import hw_5.functions_to_run


def runner(*args):
    pack = hw_5.functions_to_run
    imported_functions = [getattr(pack, func_name)
                          for func_name in dir(pack)
                          if callable(getattr(pack, func_name))]

    if args:
        functions_to_run = [func for func in imported_functions
                            if func.__name__ in args[0]]
    else:
        functions_to_run = imported_functions

    for func in functions_to_run:
        func()


if __name__ == '__main__':
    runner()

    func_to_run = ['solve_fibonacci_task']
    runner(func_to_run)

    func_to_run = ['test_digits_multiplication',
                   'solve_the_longest_word_task',
                   'is_palindrome']
    runner(func_to_run)
