# Напишите программу,
# которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

for element in range(1, 101):
    if element % 3 == 0 and element % 5 == 0:
        print("FizzBuzz")
        continue
    elif element % 3 == 0:
        print("Fizz")
        continue
    elif element % 5 == 0:
        print("Buzz")
        continue
    print(element)
