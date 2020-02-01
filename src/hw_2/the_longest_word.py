""" Find the longest word in a sentence.

A sentence has punctuation marks. There is the only one longest word
in a sentence.

Input: string.
Output: string.
"""

from string import punctuation


def get_longest_word(sentence):
    words = sentence.split()
    max_length = 0
    longest_word = ''
    for word in words:
        word = word.strip(punctuation)
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word


if __name__ == '__main__':
    print(get_longest_word("   Created by Guido van Rossum and first released "
                           "in 1991, Python's design philosophy emphasizes "
                           "code readabilityyy with its notable use of "
                           "significant whitespace. "))
