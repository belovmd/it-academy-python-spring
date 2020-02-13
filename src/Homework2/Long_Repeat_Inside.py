"""Long Repeat Inside.

But if in the first mission you needed to find repeating letters, then in
this one you should find a repeating sequence inside the substring. I have
an example for you: in a string "abababc" - "ab" is a sequence that repeats
more than once, so the answer will be "ababab"

"""


def repeat_inside(line):
    """Return first the longest repeating substring"""
    repeat_str = []
    for i in range(len(line)):
        j = i
        while len(line) > j:
            tmpl = line[i: j + 1]
            if tmpl == line[j + 1: j + 1 + len(tmpl)] and tmpl:
                if len(line) - (j + 1 + len(tmpl)) < len(tmpl):
                    repeat_str.append(tmpl * 2)
                    break
                n = 2
                for ind in range(j + 1 + len(tmpl), len(line), len(tmpl)):
                    if line[ind: ind + len(tmpl)] == tmpl:
                        n += 1
                    else:
                        break
                repeat_str.append(tmpl * n)
            j += 1
    return sorted(repeat_str, key=len, reverse=True)[0] if repeat_str else ''


if __name__ == '__main__':
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('Done!!!')
