"""Общая цена

Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество L товара Посчитайте общую цену в рублях и копейках
за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек

"""

RUBLES = int(input('Please, enter part of price per item in rubles: '))
CENTS = int(input('Please, enter part of price per item in cents: '))
count = int(input('Please, enter count of product: '))
total_rubles = RUBLES * count + (CENTS * count) // 100
total_cents = (CENTS * count) % 100
print(f'Total price {total_rubles} rubles {total_cents} cents')
