# 1. Напишите программу, которая считает общую цену. Вводится M рублей
# и N копеек цена, а также количество L товара Посчитайте общую цену
# в рублях и копейках за L товаров.
# Пример:
# Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек
# -----------------------------------------------------------------------------
def rublei(rub):
    rezultat = "рубл"
    if rub == 1:
        rezultat += "ь"
    elif rub > 1 and rub < 5:
        rezultat += "я"
    else:
        rezultat += "ей"
    return rezultat


def kopeek(kop):
    rezultat = "копе"
    if kop == 1:
        rezultat += "йка"
    elif kop > 1 and kop < 5:
        rezultat += "и"
    else:
        rezultat += 'ек'
    return rezultat


# -----------------------------------------------------------------------------
rubli = int(input("Введите цену (рубли):"))
kopeiki = int(input("Введите цену (копейки):"))
kol = int(input("Введите количество товара:"))
sum = (rubli + kopeiki / 100) * kol
rubli = int(sum // 1)
kopeiki = round((sum % 1) * 100)
print("Общая цена ", str(rubli) + " " + rublei(rubli) + " " + str(kopeiki) + " " + kopeek(kopeiki))
