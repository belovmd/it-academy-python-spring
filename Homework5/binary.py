

# 5 --------------------------------------------------------------------------
# Написать программу которая находит ближайшую степень
# двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
def power2(digit):
    digit2 = digit
    while True:
        if digit and not digit & (digit - 1):
            return digit
        if digit2 and not digit2 & (digit2 - 1):
            return digit2
        digit -= 1
        digit2 += 1


# 5 --------------------------------------------------------------------------
# Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).
def maxdiv2(digit):
    digit1 = digit
    while digit1 > 0:
        if not (digit % digit1 or digit1 & (digit1 - 1)):
            return digit1
        digit1 -= 1


print(power2(10))
print(power2(20))
print(power2(1))
print(power2(13))
print()
print(maxdiv2(10))
print(maxdiv2(16))
print(maxdiv2(12))
print(maxdiv2(17))
