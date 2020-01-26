n = int(input('Enter the number: '))
fib = 0
fib_next = 1
while n:
    fib, fib_next = fib_next, fib + fib_next
    n -= 1
print(fib)
