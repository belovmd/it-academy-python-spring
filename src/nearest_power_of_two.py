"""5.	Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)"""

number = int(input("Input number: "))
i = 1
while number > i << 1:
    i <<= 1
result = min(i, i << 1, key=lambda x: abs(x - number))
print('the nearest power of 2 for {} is {}'.format(number, result))
