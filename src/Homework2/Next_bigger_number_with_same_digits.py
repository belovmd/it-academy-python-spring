"""Next bigger number with the same digits.

You have to create a function that takes a positive integer number and
returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:
9 ==> -1
111 ==> -1
531 ==> -1

Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)

"""


def next_bigger(n):
    num = list(str(n))
    if len(num) < 2 or num == list(num[0]) * len(num):
        return -1
    for i in range(len(num) - 1, -1, -1):
        if i - 1 >= 0 and num[i] > num[i - 1]:
            st_part = num[:i]
            end_part = sorted(num[i:])
            for ind, value in enumerate(end_part[:]):
                if value > st_part[-1]:
                    st_part[-1], end_part[ind] = value, st_part[-1]
                    break
            if int(''.join(st_part + end_part)) > n:
                return int(''.join(st_part + end_part))
    else:
        return -1


if __name__ == '__main__':
    assert next_bigger(562032) == 562203
    assert next_bigger(1234567890) == 1234567908
