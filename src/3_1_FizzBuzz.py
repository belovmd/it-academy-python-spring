"""FizzBuzz
Напишите программу, которая печатает цифры от
1 до 100, но вместо чисел, кратных 3 пишет
Fizz, вместо чисел кратный 5 пишет Buzz, а
вместо чисел одновременно кратных
и 3 и 5 - FizzBuzz"""


number = 0
while number < 100:
    number += 1
    if not number % 15:
        print("FizzBuzz")
    elif not number % 3:
        print("Fizz")
    elif not number % 5:
        print("Buzz")
    else:
        print(number)
