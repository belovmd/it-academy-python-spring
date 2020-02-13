"""The Longest Palindromic

Write a function that finds the longest palindromic substring of a given
string. Try to be as efficient as possible! If you find more than one
substring, you should return the one that’s closer to the beginning.

Examples:
longest_palindromic('abc') == 'a'
longest_palindromic('abacada') == 'aba'

"""


def is_palindromic(string):
    return string == string[::-1]


def longest_palindromic(text):
    palindromics = list()
    for i in range(len(text)):
        for j in range(len(text)):
            if text[i: j + 1] and is_palindromic(text[i: j + 1]):
                palindromics.append(text[i: j + 1])
    return sorted(palindromics, key=len, reverse=True)[0]


if __name__ == '__main__':
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete!!!")
