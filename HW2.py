# 1
MN = input("Введите цену:")
MN = float(MN.replace(",", "."))
L = int(input("Введите количество:"))
total = MN * L
MN_RUB = int(total)
MN_PEN = int((total - int(total)) * 100)
print("Общая цена {} рублей {} копеек".format(MN_RUB, MN_PEN))

# 3
s = input()
s = s.replace(",", "")
s = s.replace("!", "")
s = s.replace("?", "")
s = s.replace(".", "")
s = s.split()
s.sort(key=len)
print(s[-1])

# 4
string = input()
print(string)
string_n = ''
for i in range(len(string)):
    if string_n.find(string[i]) == -1 and string[i] != ' ':
        string_n += string[i]
print(string_n)
