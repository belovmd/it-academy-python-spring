""" Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество L товара.
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""
rub = int(input('Введите количество рублей: '))
kop = int(input('Введите количество копеек: '))
kol = int(input('Введите количесво товара: '))
cost = kol * (100 * rub + kop)
print("Общая цена товаров:", cost // 100, "рублей", cost % 100, "Копеек")

"""Напишите функцию, которая будет получать 2 числа и
возвращать результат произведения этих чисел."""


def Mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print(Mult_two(3, 2))

    assert Mult_two(3, 2) == 6
    assert Mult_two(1, 0) == 0
    print("Yessssss!!!!!!")

"""Написать функцию, которая представит человека по переданным параметрам"""


def say_hi(name, age):
    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
    print('Done. Time to Check.')

"""Cоздать функцию, которая получает массив(tuple)
возвращает набор с 3 элементами - первым, третьим, вторым с конца."""


def easy_unpack(elements):
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

"""Дан массив с положительными числами и число N.
Вы должны найти N-ую степень элемента в массиве с индексом N.
Если N за границами массива, тогда вернуть -1. """


def index_power(array, n):
    return array[n] ** n if n < len(array) else -1


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check'")

"""Дан кусок текста.
Соберите все заглавные буквы в одно слово в том порядке
как они встречаются в куске текста. """


def find_message(text: str) -> str:
    cap = ''
    for x in text:
        if x.isupper():
            cap += x
    return cap
    if cap == '':
        print('Nothing')
    else:
        print(cap)


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check'")

"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""

str = str(input("enter"))
print(str)

list = str.split()

id = 0

for i in range(1, len(list)):
    if len(list[id]) < len(list[i]):
        id = i

print(list[id])

"""Вводится строка. Требуется удалить из нее повторяющиеся символы и
все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"""

st = input('enter: ')
newSt = ''
for i in st:
    if i not in newSt and i != ' ':
        newSt += i
print(newSt)

"""Посчитать количество строчных (маленьких) и
прописных (больших) букв в введенной строке.
Учитывать только английские буквы."""

word = input()
mal = 0
bol = 0
for i in word:
    if 'a' <= i <= 'z':
        mal += 1
    elif 'A' <= i <= 'Z':
        bol += 1
    else:
        pass
print(mal)
print(bol)

"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""

fib1 = 1
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)

"""
Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

s = input()

Palindrome = len(s)

for i in range(1 // 2):
    if s[i] != s[-1 - i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")
