"""Написать программу которая
находит ближайшую степень двойки
к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


number = int(input("Insert the number: "))
right_point = 1

while number > right_point:
    right_point <<= 1
left_point = right_point >> 1

if abs(right_point - number) \
        <= abs(number - left_point):
    print(right_point)
else:
    print(left_point)
