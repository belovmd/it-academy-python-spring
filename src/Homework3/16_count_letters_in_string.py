"""Count all letters in input string

Задача из лекции:
Посчитать количество каждой буквы в введенной строке.

"""


def count_letters_string(string):
    """Count all letters in string"""
    cnt_dct = dict()
    for letter in string:
        cnt_dct[letter] = cnt_dct.get(letter, 0) + 1
    return cnt_dct


if __name__ == '__main__':
    inp_string = input('Enter your string:\n')
    print(count_letters_string(inp_string))
