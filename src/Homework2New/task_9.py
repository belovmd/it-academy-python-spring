def duplicate_count(text):
    """Instructions

    Write a function that will return the count
    of distinct case-insensitive alphabetic characters
    and numeric digits that occur more than once
    in the input string. The input string can be assumed
    to contain only alphabets (both uppercase and
    lowercase) and numeric digits.
    """
    count = 0
    test_dict = {}
    for char in text.lower():
        test_dict[char] = 0
    for char in text.lower():
        test_dict[char] += 1
    for key, value in test_dict.items():
        if value > 1:
            count += 1
    return count


if __name__ == '__main__':
    test_string = input('Enter string: ')
    print(duplicate_count(test_string))
