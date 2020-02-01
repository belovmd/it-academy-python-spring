""" Remove repeating chars and whitespaces from a string.

Example:
Input: 'abc cde def'.
Output: 'abcdef'
"""


def remove_repeating_chars(string):
    word = string.replace(' ', '')
    chars_list = []
    for char in word:
        if char not in chars_list:
            chars_list.append(char)
    return ''.join(chars_list)


if __name__ == '__main__':
    print(remove_repeating_chars("abc cde def"))
