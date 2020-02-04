"""Roman Numerals Helper.

Task
Create a RomanNumerals class that can convert a roman numeral to and from
an integer value. It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.
Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
| Symbol | Value |
| I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 |

assert(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
assert(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')

assert(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
assert(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')

"""


class RomanNumerals(object):
    roman_nums = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    @classmethod
    def to_roman(cls, n):
        """Convert digit to RomanNumeral."""
        romans = sorted(cls.roman_nums.items(), key=lambda i: i[1],
                        reverse=True)
        roman_num = ''
        for r_num, value in romans:
            roman_num += r_num * (n // value)
            n -= value * (n // value)
        return roman_num

    @classmethod
    def from_roman(cls, roman_num):
        """Convert RomanNumeral to digit."""
        digit_num = 0
        while roman_num:
            if roman_num[:2] in cls.roman_nums.keys():
                digit_num += cls.roman_nums.get(roman_num[:2])
                roman_num = roman_num[2:]
            else:
                digit_num += cls.roman_nums.get(roman_num[0])
                roman_num = roman_num[1:]
        return digit_num


if __name__ == '__main__':
    assert RomanNumerals.to_roman(1000) == 'M'
    assert RomanNumerals.to_roman(1990) == 'MCMXC'

    assert RomanNumerals.from_roman('XXI') == 21
    assert RomanNumerals.from_roman('MMVIII') == 2008
