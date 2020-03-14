"""Даны два списка чисел. Посчитайте,
сколько различных чисел входит
только в один из этих списков
"""


input_1 = str(input("Insert first numbers: "))
input_2 = str(input("Insert second numbers: "))

select_the_list = int(input("Insert number "
                            "of the list: "))

if select_the_list == 1:
    lst = input_1.split()
    lst = [int(element) for element in lst]

elif select_the_list == 2:
    lst = input_2.split()
    lst = [int(element) for element in lst]

else:
    print("You did not select the list of numbers.")
    raise SystemExit

dct_numbers = {element: lst.count(element)
               for element in lst}

print("The number of different numbers "
      "in list {number}:"
      .format(number=select_the_list),
      len(dct_numbers))
