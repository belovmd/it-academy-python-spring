"""1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество L товара.
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

price_ruble = int(input("Введите стоимость в рублях: "))
price_cents = int(input("Введите стоимость в копейках: "))
count_items = int(input("Введите количество товаров: "))
price_itog = (price_ruble * 100 + price_cents) * count_items  # Цена в копейках
price_cents = price_itog % 100
price_ruble = int((price_itog - price_cents) / 100)
print("Общая цена %s рублей %s копеек" % (price_ruble, price_cents))
