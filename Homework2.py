# 1
MN = float(input("Введите цену:"))
L = int(input("Введите количество"))
total = str(MN * L)
print("Общая цена " + str(int(MN + L)) + " рублей" + " " + total[-15:-13] + " копеек")

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
