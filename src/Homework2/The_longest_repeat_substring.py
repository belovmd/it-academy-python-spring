"""Length the longest substring that consists of the same char.

This mission is the first one of the series. Here you should find the length
of the longest substring that consists of the same letter. For example, line
"aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c"
and "aaaa". The last substring is the longest one, which makes it the answer.

assert long_repeat('sdsffffse') == 4
assert long_repeat('ddvvrwwwrggg') == 3

"""
from itertools import groupby


def long_repeat_m1(line: str) -> int:
    groups = [list(g) for k, g in groupby(line)]
    return max((sum(1 for _ in gr) for gr in groups), default=0)


def long_repeat_m2(line: str) -> int:
    if line:
        max_len = cur_len = 1
        cur_char = ''
        for char in line:
            if char == cur_char:
                cur_len += 1
            else:
                cur_char = char
                cur_len = 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
    return 0


if __name__ == '__main__':
    assert long_repeat_m1('sdsffffse') == 4
    assert long_repeat_m1('ddvvrwwwrggg') == 3
    assert long_repeat_m1('abababaab') == 2
    assert long_repeat_m1('') == 0
    print('Test method 1 passed. Done!!!')
    assert long_repeat_m2('sdsffffse') == 4
    assert long_repeat_m2('ddvvrwwwrggg') == 3
    assert long_repeat_m2('abababaab') == 2
    assert long_repeat_m2('') == 0
    print('Test method 2 passed. Done!!!')
