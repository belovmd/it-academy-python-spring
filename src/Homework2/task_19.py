def parse_int(string):
    """Instructions

    In this function we want to convert a
    string into an integer. The strings
    simply represent the numbers in words.
    """
    dict = {'zero': 0, 'one': 1, 'two': 2,
            'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13,
            'fourteen': 14, 'fifteen': 15,
            'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19,
            'twenty': 20, 'thirty': 30, 'forty': 40,
            'fifty': 50, 'sixty': 60, 'seventy': 70,
            'eighty': 80, 'ninety': 90, 'hundred': 100,
            'thousand': 1000, 'million': 1000000}

    list = string.replace(' and', '').replace('-', ' ').split()
    for ind, char in enumerate(list):
        list[ind] = dict[char]
    sum = 0
    counter_thousand = 0
    for ind, num in enumerate(list):
        if num < 100:
            sum += num
        if num % 100 == 0:
            sum *= num
        if num == 1000:
            counter_thousand = sum
            sum = 0
    return counter_thousand + sum


if __name__ == '__main__':
    assert parse_int('one') == 1
    assert parse_int('twenty') == 20
    assert parse_int('two hundred forty-six') == 246
