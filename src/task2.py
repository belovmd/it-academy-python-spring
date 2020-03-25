def dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        file = open('text.txt', 'a')
        file.write(str(res) + '\n')
        file.close()
        return res
    return wrapper


@dec
def numb(num):
    return num


numb(5)
numb(6)
numb(1)

f = open('text.txt')
print(f.read())
f.close()
