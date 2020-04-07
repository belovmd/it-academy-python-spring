""" Decorator

Variant 3: homework 3 task 4
"""


from itertools import combinations

NUMBER_OF_ATTEMPTS = 3


class TooManyErrors(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


def run_until_no_err(max_attempts):
    attempts_used = 0

    def decorator(func):
        def safe_wrapper():
            nonlocal attempts_used
            nonlocal max_attempts
            while attempts_used < max_attempts:
                attempts_used += 1
                try:
                    result = func()
                    return result
                except ValueError as err:
                    if attempts_used == max_attempts:
                        raise TooManyErrors('Too many errors!')
                    else:
                        print('Error occurred, try one more time.', type(err))
        return safe_wrapper
    return decorator


@run_until_no_err(NUMBER_OF_ATTEMPTS)
def count_pairs():
    print('Input elements:')
    elements = [int(number) for number in input().strip().split()]

    all_combinations = list(combinations(elements, 2))
    equal_pairs = [el for el in all_combinations if el[0] == el[1]]
    return len(equal_pairs)


if __name__ == '__main__':
    try:
        print(count_pairs())
    except TooManyErrors as error:
        print(error)
