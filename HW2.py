# for #3
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
