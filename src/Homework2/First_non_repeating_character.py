"""First non-repeating character.

Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the
string. As an added challenge, upper- and lowercase letters are considered
the same character, but the function should return the correct case for the
initial letter.
For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty
string ("") or None -- see sample tests.

Test.assert_equals(first_non_repeating_letter('a'), 'a')
Test.assert_equals(first_non_repeating_letter('stress'), 't')
Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

"""
from collections import Counter


def first_non_repeating_letter(string):
    lower_str = string.lower()
    cnt = Counter(lower_str)
    temp_list = list()
    for k, v in cnt.items():
        if v == 1:
            temp_list.append(k)
    if temp_list:
        indexes = []
        for char in temp_list:
            indexes += [lower_str.index(char)]
        return string[min(indexes)]
    return ''


if __name__ == '__main__':
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('ke ksep s') == 'p'
    assert first_non_repeating_letter('rrjouo') == 'j'
