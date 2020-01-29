# 1
MN = float(input("Введите цену:"))
L = int(input("Введите количество"))
total = str(MN * L)
a = str(int(MN + L))
b = total[-15:-13]
print("Общая цена " + a + " рублей" + " " + b + " копеек")

# 3
s = input()
s = s.replace(",", "")
s = s.replace("!", "")
s = s.replace("?", "")
s = s.replace(".", "")
s = s.split()
s.sort(key=len)
print(s[-1])
