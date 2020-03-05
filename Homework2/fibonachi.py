# Show first n fibonacci numbers
n = int(input("Введите n:"))
f_prev = 0
f_curr = 1
for i in range(n - 1):
    f_prev, f_curr = f_curr, f_curr + f_prev

print(f_prev)
