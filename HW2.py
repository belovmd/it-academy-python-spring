# for №3
import string

# 1
MN = input("Введите цену:")
MN = float(MN.replace(",", "."))
L = int(input("Введите количество:"))
total = MN * L
MN_RUB = int(total)
MN_PEN = int((total - int(total)) * 100)
print("Общая цена {} рублей {} копеек".format(MN_RUB, MN_PEN))

# 3
my_str = input()
my_punc = str.maketrans(dict.fromkeys(string.punctuation))
my_word = my_str.translate(my_punc).split()
my_word.sort(key=len)
print(my_word[-1])

# 4
string = input()
string_n = ''
for i in range(len(string)):
    if string_n.find(string[i]) == -1 and string[i] != ' ':
        string_n += string[i]
print(string_n)

# 5
my_str = input()
catalog = {}
for let in my_str:
    if 'a' <= let <= 'z' or 'A' <= let <= 'Z':
        if let in catalog:
            catalog[let] = catalog[let] + 1
        else:
            catalog[let] = 1
for k in catalog:
    print(k, ':', catalog[k])

# n-th Fibonacci number
fib1 = fib2 = 1
n = int(input())
if n < 2:
    quit()
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

# Palindrome (True or False)
num_pal = input()
rev_num_pal = num_pal[::-1]
if num_pal == rev_num_pal:
    print('True')
else:
    print('False')
