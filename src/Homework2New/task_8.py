def duplicate_encode(word):
    """Instructions

    The goal of this exercise is to convert
    a string to a new string where each character
    in the new string is "(" if that character
    appears only once in the original string, or ")"
    if that character appears more than once in the
    original string. Ignore capitalization when
    determining if a character is a duplicate.
    """
    output_string = ''
    test_dict = {}
    # Create a dict with keys consists from word chars
    for w in word.lower():
        test_dict[w] = 0
    # Counting of elements equals
    for w in word.lower():
        test_dict[w] += 1
    # Output_string_generating
    for w in word.lower():
        output_string += '(' if test_dict[w] == 1 else ')'
    return output_string


if __name__ == '__main__':
    test_word = input('Enter test word:')
    print(duplicate_encode(test_word))
