def word_count(test_string):
    """Different words in string

    :param test_string: string of words separated from each other with
           whitespaces and symbols of the end of line
    :return: number of different words in test_string
    """
    return len(set(test_string.split()))


if __name__ == '__main__':
    assert(word_count('a   a b  \n\n\n c\n\na\nh\ns w  a \n\n f')) == 7
    assert(word_count('    \n\n   \n \n   ')) == 0
    assert word_count('   \n\na\n\n    \n   ') == 1
