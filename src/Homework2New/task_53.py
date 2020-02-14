def longest_palindromic(a):
    """The longest palindromic"""
    result = ''
    for i in range(len(a)):
        for j in range(i, len(a)):
            tmp_val = a[i:j + 1:1]
            if tmp_val == tmp_val[::-1] and len(a[i:j + 1:1]) > len(result):
                result = a[i:j + 1:1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abacada'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
