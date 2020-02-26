"""Количество строчных и прописных букв.

Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.

"""

import re


def has_cyrillic(string):
    return bool(re.search(r'[а-яА-ЯЁё]', string))


def count_low_and_up_chars(string):
    count_low_chars = count_up_chars = 0
    for char in string:
        if not has_cyrillic(char) and char.isalpha():
            if char.islower():
                count_low_chars += 1
            else:
                count_up_chars += 1
    return count_low_chars, count_up_chars


if __name__ == '__main__':
    # simple test
    assert count_low_and_up_chars('Ak ! . d иЁ у tRy я') == (4, 2)

    inp_string = input('Enter your string: ')
    count_low_chars, count_up_chars = count_low_and_up_chars(inp_string)
    print(f'Count of lower chars = {count_low_chars}\n'
          f'Count of upper chars = {count_up_chars}')
