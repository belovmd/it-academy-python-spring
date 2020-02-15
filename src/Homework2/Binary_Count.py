"""Binary_Count.

For the Robots the decimal format is inconvenient. If they need to count to
"1", their computer brains want to count it in the binary representation of
that number. You can read more about binary here. You are given a number
(a positive integer). You should convert it to the binary format and count
how many unities (1) are in the number spelling. For example: 5 = 0b101
ontains two unities, so the answer is 2.

Input: A number as a positive integer.
Output: The quantity of unities in the binary form as an integer.

"""


def binary_count(number: int) -> int:
    return sum(map(int, str(bin(number)).strip('0b')))


if __name__ == '__main__':
    assert binary_count(4) == 1
    assert binary_count(15) == 4
    assert binary_count(1) == 1
    assert binary_count(1022) == 9
    print("All tests passed!!!")
