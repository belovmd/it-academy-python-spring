def fizzbuzz():
    """Task FizzBuzz

    Create sequence with numbers from 1 to 100, but instead numbers
    multiple of 3 print Fizz, instead numbers multiple of 5 print Buzz,
    instead numbers multiple both of 3 and 5 print FizzBuzz
    """
    sequence = (
        [nmb if (nmb % 3 != 0 and nmb % 5 != 0)
         else 'FizzBuzz' if (nmb % 3 == 0 and nmb % 5 == 0)
         else 'Fizz' if (nmb % 3 == 0)
         else'Buzz' for nmb in range(1, 101)])
    return sequence


if __name__ == '__main__':

    for element in fizzbuzz():
        print(element, end=' ')
