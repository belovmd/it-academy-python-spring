def fibonacci(n):
    """Fibonacci.

    :param n: index of element from fibonacci sequence
    :return: fibonacci value

    """
    previous, next = 0, 1
    for _ in range(10):
        previous, next = next, previous + next
    return previous


assert fibonacci(10) == 55
