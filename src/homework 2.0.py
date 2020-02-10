m = int(input("Рубли"))
c = int(input("Копейки"))
n = int(input("Колличесво предметов"))
cost = n * (100 * m + c)
print("Общая цена", cost // 100, "рублей", cost % 100, "копеек")
3