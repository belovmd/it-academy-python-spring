"""Count Consecutive Summers.

Positive integers can be expressed as sums of consecutive positive integers
in various ways. For example, 42 can be expressed as such a sum in four
different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.
As the last solution (d) shows, any positive integer can always be trivially
expressed as a singleton sum that consists of that integer alone.

Example:

count_consecutive_summers(42) == 4
count_consecutive_summers(99) == 6

"""


def count_consecutive_summers(num):
    count = 0
    for begin in range(1, num + 1):
        digit = 0
        while digit < num:
            digit += begin
            begin += 1
        if digit == num:
            count += 1
    return count


def count_consecutive_summers(num):
    count = 1 + (num%2)*(not not num//2)
    for i in range(3,1+num//2,2):
        if not num%i:
            count += 1
    return count


if __name__ == '__main__':
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Done")
