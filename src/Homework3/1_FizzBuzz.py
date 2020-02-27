"""FizzBuzz.

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz.

"""


def fizz_buzz():
    return ['Fizz' * (a % 3 == 0) + (
            'Buzz' * (a % 5 == 0)) or a for a in range(1, 101)]


if __name__ == '__main__':
    for digit in fizz_buzz():
        print(digit)
