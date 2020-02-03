def productfib(prod):
    """Instructions

    prod:: given integer natural argument
    return:: list with two fibonacci numbers
    whose multiplication >= prod and flag ='False'
    if multiplication > prod, flag = 'True'
    if multiplication = prod
    prod = 45678
    return = [233, 377, False]
    """
    print(prod)
    fib = 0
    fib_next = 1
    while fib * fib_next < prod:
        fib, fib_next = fib_next, fib + fib_next
    return [fib, fib_next, fib * fib_next == prod]


if __name__ == '__main__':
    print(productfib(45678))
    print(productfib(33552))
