"""Calculate n-th Fibonacci number.

Input: n.
Output: n-th Fibonacci number.
"""


def solve_fibonacci_task():

    def fibonacci(n: int):
        first = 1
        second = 1
        if n >= 1:
            print(first)
        if n >= 2:
            print(second)
        if n >= 3:
            i = 2
            while i < n:
                current = first + second
                print(current)
                first, second = second, current
                i += 1

    fibonacci(5)


if __name__ == '__main__':
    solve_fibonacci_task()
