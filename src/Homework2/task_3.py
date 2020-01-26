def is_isogram(string):
    """Instruction here

    An isogram is a word that has no repeating letters,
    consecutive or non-consecutive. Implement a function
    that determines whether a string that contains only
    letters is an isogram. Assume the empty string is an
    isogram. Ignore letter case.
    """
    test_set = set(string.lower())
    if len(test_set) != len(string):
        return False
    return True


if __name__ == '__main__':
    print(is_isogram(input('Enter string: ')))
