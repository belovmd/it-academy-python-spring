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


assert count_low_and_up_chars('Ak ! . d иЁ у tRy я') == (4, 2)


if __name__ == '__main__':
    inp_string = input('Enter your string: ')
    count_low_chars, count_up_chars = count_low_and_up_chars(inp_string)
    print(f'Count of lower chars = {count_low_chars}\n'
          f'Count of upper chars = {count_up_chars}')
