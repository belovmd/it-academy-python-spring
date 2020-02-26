"""Find number in Fibonacci sequence by index

This task can be realized by several methods such as reсursion
and different loops (cycles for, while)

"""


def fibonacci_loop_for(n):
    """Find number in Fibonacci sequence by index n using cycle for"""
    previous, next = 0, 1
    for _ in range(10):
        previous, next = next, previous + next
    return previous


def fibonacci_loop_while(n):
    """Find number in Fibonacci sequence by index n using cycle while"""
    previous, next = 0, 1
    while n > 0:
        previous, next = next, previous + next
        n -= 1
    return previous


def fibonacci_recurcion(n):
    """Find number in Fibonacci sequence by index n using recursion"""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci_recurcion(n - 2) + fibonacci_recurcion(n - 1)


if __name__ == '__main__':
    assert fibonacci_loop_for(10) == 55
    assert fibonacci_loop_while(10) == 55
    assert fibonacci_recurcion(10) == 55
