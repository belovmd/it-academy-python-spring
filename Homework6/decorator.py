N = 1000

def decor(func):

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

fibonachi_previous = 0
fibonachi_current = 1
@decor
for i in range(n - 1):
    fibonachi_save = fibonachi_current
    fibonachi_current += fibonachi_previous
    fibonachi_previous = fibonachi_save
print(fibonachi_previous)


