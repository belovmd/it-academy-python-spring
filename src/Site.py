# https://py.checkio.org/
#
# 1) You are given a chunk of text. Gather all capital letters in one word in
# the order that they appear in the text.#
# For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect
# all of the capital letters, we get the message "HELLO".#
# Input: A text as a string (unicode).#
# Output: The secret message as a string or an empty string.


def find_message(text: str) -> str:
    """Find a secret message"""
    message = ""
    for i in range(len(text)):
        if text[i].isupper():
            message += text[i]
    return message


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert find_message(
        "How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool"
        "rewards!")


# 2) In this mission you should write a function that introduces a
# person with the given parameter's attributes.#
# Input: Two arguments. String and positive integer.#
# Output: String.


def say_hi(name: str, age: int) -> str:
    # your code here
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert say_hi("Alex",
                  32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank",
                  68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')


# 3) You are given an array with positive numbers and a number N. You should
# find the N-th power of the element in the array with the index N. If N is
# outside of the array, then return -1. Don't forget that the first element has
# the index 0.
# Input: Two arguments. An array as a list of integers and a number as a
# integer.#
# Output: The result as an integer.


def index_power(array: list, n: int) -> int:
    if n >= len(array):
        return -1
    else:
        return array[n] ** n


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool"
        "rewards!")


# 4) Write a function that will receive 2 numbers as input and it should return
# the multiplication of these 2 numbers.#
# Input: Two arguments. Both are int#
# Output: Int.


def mult_two(a, b):
    # your code here
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


# 5) You are given an array of integers. You should find the sum of the
# integers with even indexes (0th, 2nd, 4th...). Then multiply this summed
# number and the final element of the array together. Don't forget that the
# first element has an index of 0.
# For an empty array, the result will always be 0 (zero).
# Input: A list of integers.
# Output: The number as an integer.

def checkio(array):
    s = 0
    if len(array) == 0:
        return 0
    else:
        for i in range(0, len(array), 2):
            s += array[i]
        return (array[len(array) - 1]) * s


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print(
        "Coding complete? Click 'Check' to review your tests and earn"
        "cool rewards!")
