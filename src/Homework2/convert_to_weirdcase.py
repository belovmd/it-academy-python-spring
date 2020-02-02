"""Task: convert string to weirdcase.

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
and returns the same string with all even indexed characters in each word
upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even,
therefore that character should be upper cased. The passed in string will
only consist of alphabetical characters and spaces(' '). Spaces will only be
present if there are multiple words. Words will be separated by a single
space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

"""
import unittest


def to_weird_case_word(word):
    """Convert word to WeirdCase."""
    return ''.join([char.upper() if ind % 2 == 0 else char
                    for ind, char in enumerate(word.strip().lower())])


def to_weird_case(string):
    """Convert string to WeirdCase."""
    return ' '.join([to_weird_case_word(word) for word in string.split()])


class TestConvertToWeirdCase(unittest.TestCase):
    def test_to_weirdcase_convert(self):
        self.assertEqual(to_weird_case('floppy'), 'FlOpPy')
        self.assertEqual(to_weird_case('Weird string case'),
                         'WeIrD StRiNg CaSe')


if __name__ == '__main__':
    unittest.main()
