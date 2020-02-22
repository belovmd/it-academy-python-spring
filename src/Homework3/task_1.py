def fizzbuzz():
    """Task FizzBuzz

    Create sequence with numbers from 1 to 100, but instead numbers
    multiple of 3 print Fizz, instead numbers multiple of 5 print Buzz,
    instead numbers multiple both of 3 and 5 print FizzBuzz
    """
    sequence = []
    for x in range(1, 101):
        sequence.append('Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0) or x)
    return sequence


if __name__ == '__main__':

    for element in fizzbuzz():
        print(element, end=' ')
