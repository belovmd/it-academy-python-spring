"""Даны два списка чисел. Посчитайте,
сколько различных чисел входит
только в один из этих списков
"""


input_1 = str(input("Insert first numbers: "))
input_2 = str(input("Insert second numbers: "))

select_the_list = int(input("Insert number "
                            "of the list: "))

if select_the_list == 1:
    selected, not_selected = input_1, input_2

elif select_the_list == 2:
    selected, not_selected = input_2, input_1

else:
    print("You did not select the list of numbers.")
    raise SystemExit

selected = {int(element) for element in selected.split()}
not_selected = {int(element) for element in not_selected.split()}

print("The number of different numbers "
      "in list {number}:"
      .format(number=select_the_list),
      len(selected.difference(not_selected)))
