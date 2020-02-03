n = int(input('Enter the number: '))
fib, fib_next = 0, 1
while n:
    fib, fib_next = fib_next, fib + fib_next
    n -= 1
print(fib)
