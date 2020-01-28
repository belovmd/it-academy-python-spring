# Show first n fibonacci numbers
n = int(input("Введите n:"))
fibonachi_previous = 0
fibonachi_current = 1
for i in range(n - 1):
    fibonachi_save = fibonachi_current
    fibonachi_current += fibonachi_previous
    fibonachi_previous = fibonachi_save
print(fibonachi_previous)
