# Напишите программу,
# которая считает общую цену.
# Вводится M рублей и N копеек цена,
# а также количество L товара.
# Посчитайте общую цену в рублях и копейках за L товаров.

rubles = int(input("Enter rubles: "))
kopecks = int(input("Enter kopecks: "))
count = int(input("Enter counts product: "))
result_rubles = rubles * count + kopecks * count // 100
result_kopecks = kopecks * count % 100
print("{0} rubles {1} kopecks for {2} product"
      .format(result_rubles, result_kopecks, count))
