""" FizzBuzz

Print numbers from 1 to 100.
If a number is divisible by 3 and by 5 print 'FizzBuzz'.
If a number is divisible by 3 print 'Fizz'.
if a number is divisible by 5 print 'Buzz'.
"""


def fizz_buzz(n):
    return (n % 3 == 0 and n % 5 == 0 and 'FizzBuzz') or (
            n % 3 == 0 and 'Fizz') or (
            n % 5 == 0 and 'Buzz') or n


if __name__ == '__main__':
    assert fizz_buzz(15) == "FizzBuzz", "15 is divisible by 3 and 5"
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(7) == 7, "7 is not divisible by 3 or 5"

    result = [fizz_buzz(number) for number in range(1, 101)]
    print(*result)
