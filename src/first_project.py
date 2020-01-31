# Напишите программу,
# которая считает общую цену.
# Вводится M рублей и N копеек цена,
# а также количество L товара.
# Посчитайте общую цену в рублях и копейках за L товаров.

rubles = int(input("Enter rubles: "))
kopecks = int(input("Enter kopecks: "))
count = int(input("Enter counts product: "))
result_rubles = rubles * count
result_kopecks = kopecks * count
while result_kopecks >= 100:
    result_rubles += 1
    result_kopecks -= 100
print("{0} rubles {1} kopecks for {2} product"
      .format(result_rubles, result_kopecks, count))
