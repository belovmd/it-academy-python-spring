"""6. Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)."""

number = int(input("Input number: "))
i = 1
while number % i == 0:
    i <<= 1
print("for the number {} the maximum divisor in power 2 is {}"
      .format(number, i >> 1))
