"""Даны два списка чисел. Посчитайте,
сколько различных чисел содержится
одновременно как в первом списке,
так и во втором.
"""

input_1 = str(input("Insert first numbers: "))
input_2 = str(input("Insert second numbers: "))

list_1 = input_1.split()
list_2 = input_2.split()

list_1 = [int(element) for element in list_1]
list_2 = [int(element) for element in list_2]

list_1.extend(list_2)

dct_numbers = {element: list_1.count(element)
               for element in list_1}

print("The number of different numbers "
      "in lists: ", len(dct_numbers))
