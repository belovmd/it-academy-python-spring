def checkio(f, g):
    """Function validator

    Two functions f and g are provided as inputs to checkio.
    The first function f is the primary function and the second function g is
    the backup. Use your coding skills to return a third function h which
    returns the same output as f unless f raises an exception or returns None.
    In this case h should return the same output as g. If both f and g raise
    exceptions or return None, then h should return None.

    As a second output, h should return a status string indicating whether
    the function values are the same and if either function erred. A function
    errs if it raises an exception or returns a null value (None).

    The status string should be set to: "same" if f and g return the same
    output and neither errs, "different" if f and g return different outputs
    and neither errs, "f_error" if f errs but not g, "g_error" if g errs but
    not f, or "both_error" if both err.

    :param f: functions f (primary)
    :param g: functions g (back up function)
    :return: A function h which takes arbitrary inputs and returns a two-tuple
    """
    def h(*args, **kwargs):
        """Inner function"""
        try:
            f_result = f(*args, **kwargs)
        except Exception:
            f_result = None
        try:
            g_result = g(*args, **kwargs)
        except Exception:
            g_result = None

        if f_result == g_result and f_result is None:
            return None, 'both_error'

        if f_result is not None:
            if f_result == g_result:
                return f_result, 'same'
            if f_result != g_result and g_result is not None:
                return f_result, 'different'
            if g_result is None:
                return f_result, 'g_error'

        if g_result is not None:
            return g_result, 'f_error'

        return None, 'both_error'

    return h


if __name__ == '__main__':

    assert checkio(
        lambda x, y: x + y,
        lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 3) == (4, 'same')

    assert checkio(
        lambda x, y: x + y,
        lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 2) == (3, 'same')

    assert checkio(
        lambda x, y: x + y,
        lambda x, y:
        (x ** 2 - y ** 2) / (x - y))(1, 1.01) == (2.01, 'different')

    assert checkio(
        lambda x, y: x + y,
        lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1) == (2, 'g_error')

    # Remove odds from list

    def f(nums):
        return [x for x in nums if ~x % 2]

    def g(nums):
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums.pop(i)
        return nums

    assert checkio(f, g)([2, 4, 6, 8]) == ([2, 4, 6, 8], 'same')
    assert checkio(f, g)([2, 3, 4, 6, 8]) == ([2, 4, 6, 8], 'g_error')

    # Fizz Buzz
    assert checkio(
        lambda n:
        ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
        lambda n:
        ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(6) == \
        ('Fizz', 'same')

    assert checkio(
        lambda n:
        ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
        lambda n:
        ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(30) == \
        ('Fizz Buzz', 'same')

    assert checkio(
        lambda n:
        ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
        lambda n:
        ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(7) == \
        ('7', 'different')
