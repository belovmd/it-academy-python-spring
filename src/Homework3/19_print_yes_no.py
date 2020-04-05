"""Print YES or NO

Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это
число ранее встречалось в последовательности или NO, если не встречалось.

"""


def yes_no(str_numbers_sequence):
    """Print 'YES' if number repeated in string else print 'NO'"""
    numbers = str_numbers_sequence.split()
    unique = set(numbers)
    clean_numbers = numbers[:]
    for item in unique:
        if item in clean_numbers:
            clean_numbers.remove(item)
    for item in numbers:
        print(f'{item} - YES' if item in clean_numbers else f'{item} - NO')


if __name__ == '__main__':
    inp_str = input('Enter numbers separated by whitespaces:\n')
    yes_no(inp_str)
