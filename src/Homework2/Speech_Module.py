"""Speech Module.

You must write function which takes digit number and output string
representation this digit by words. All the words in the string must be
separated by exactly one space character. Be careful with spaces -- it's
hard to see if you place two spaces instead one.

"""
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def speech_module(n):
    hundr = n // 100
    tens = (n - hundr * 100) // 10
    units = (n - hundr * 100 - tens * 10)
    str_repr = f'{FIRST_TEN[hundr - 1]} {HUNDRED} ' if hundr else ''
    if tens >= 2:
        str_repr += OTHER_TENS[tens - 2] + ' '
    if 0 < tens < 2:
        str_repr += SECOND_TEN[((tens * 10) + units) - 10] + ' '
        return str_repr.strip()
    if units:
        str_repr += FIRST_TEN[units - 1]
    return str_repr.strip()


if __name__ == '__main__':
    assert speech_module(4) == 'four', "1st example"
    assert speech_module(133) == 'one hundred thirty three', "2nd example"
    assert speech_module(12) == 'twelve', "3rd example"
    assert speech_module(101) == 'one hundred one', "4th example"
    assert speech_module(212) == 'two hundred twelve', "5th example"
    assert speech_module(40) == 'forty', "6th example"
    assert not speech_module(212).endswith(' ')
    print('Done!')
