# Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

number = int(input("Enter number: "))
temp = number
reverted_number = 0
while temp > 0:
    reverted_number *= 10
    reverted_number += temp % 10
    temp //= 10

if reverted_number == number:
    print("number palindrome")
else:
    print("number not palindrome")
