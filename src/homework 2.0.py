m = int(input("Рубли"))
n = int(input("Копейки"))
l = int(input("Колличесво предметов"))
cost = l * (100 * m + n)
print("Общая цена", cost // 100, "рублей", cost % 100, "копеек")
