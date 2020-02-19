# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
def fizzbuzz():
    for i in range(1, 101):
        WhatPrint = ""
        if i % 3 == 0:
            WhatPrint += "Fizz"
        if i % 5 == 0:
            WhatPrint += "Buzz"
        if not WhatPrint:
            WhatPrint = i
        print(WhatPrint)


def listpractice():
    list1 = [element + element2 for element in "ab" for element2 in "bcd"]
    print(list1)
    print(list1[::2])
    list2 = [element + 'a' for element in "1234"]
    print(list2)
    print("{}, list = {}".format(list2.pop(list2.index('2a')), list2))
    list3 = list2.copy()
    

# fizzbuzz()
listpractice()
