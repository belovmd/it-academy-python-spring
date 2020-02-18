"""
https://py.checkio.org/mission/fizz-buzz/solve/

"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: A number as an integer.
Output: The answer as a string.
Precondition: 0 < number ≤ 1000
"""


def get_fizz_buzz(number: int) -> str:
    is_divisible_by_3 = False
    is_divisible_by_5 = False
    if number % 3 == 0:
        is_divisible_by_3 = True
    if number % 5 == 0:
        is_divisible_by_5 = True

    if is_divisible_by_3 and is_divisible_by_5:
        result = "Fizz Buzz"
    elif is_divisible_by_3:
        result = "Fizz"
    elif is_divisible_by_5:
        result = "Buzz"
    else:
        result = str(number)
    return result


if __name__ == '__main__':
    print('Example:')
    print(get_fizz_buzz(15))

    assert get_fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert get_fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert get_fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert get_fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"
