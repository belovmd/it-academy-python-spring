# Определите, является ли число палиндромом (читается слева направо и справа
# налево одинаково).  Число положительное целое, произвольной длины. Задача
# требует работать только с числами (без конвертации числа в строку или
# что-нибудь еще)
number = int(input('Enter number '))
new_number = number
rev_number = 0
while number:
    rev_number *= 10
    dig = number % 10
    number = (number - dig) // 10
    rev_number += dig
print('Polindrome' * (new_number == rev_number) or 'Not polindrome')
