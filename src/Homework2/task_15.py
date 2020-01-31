def mix(s1, s2):
    """Instructions

    Given two strings s1 and s2, we want to visualize
    how different the two strings are. We will only
    take into account the lowercase letters (a to z).
    First let us count the frequency of each lowercase
    letters in s1 and s2.
    """
    s = 'qwertyuioplkjhgfdsazxcvbnm'
    list_result = []
    dict_s1, dict_s2 = map(lambda s: {a: 0 for a in s}, [s, s])
    for char in s1:
        if char.islower():
            dict_s1[char] += 1
    for char in s2:
        if char.islower():
            dict_s2[char] += 1
    for key in dict_s1.keys():
        if dict_s1[key] > 1 and dict_s1[key] > dict_s2[key]:
            list_result.append('1:' + key * dict_s1[key])
        if dict_s2[key] > 1 and dict_s2[key] > dict_s1[key]:
            list_result.append('2:' + key * dict_s2[key])
        if dict_s1[key] > 1 and dict_s1[key] == dict_s2[key]:
            list_result.append('=:' + key * dict_s1[key])
    list_result = sorted(list_result, key=lambda s: (-len(s), s))
    return '/'.join(list_result)


if __name__ == '__main__':
    assert (mix("Are they here", "yes, they "
                                 "are here") == "2:eeeee/2:yy/=:hh/=:rr")

    assert (mix("looping is fun but dangerous",
                "less dangerous than coding") == "1:ooo/1:uuu/2:sss"
                                                 "/=:nnn/1:ii/2:aa"
                                                 "/2:dd/2:ee/=:gg")

    assert (mix(" In many "
                "languages", " there's a "
                "pair of functions") == "1:aaa/1:nnn/1:gg"
                                        "/2:ee/2:ff/2:ii/2:oo/"
                                        "2:rr/2:ss/2:tt")

    assert (mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo")

    assert (mix("codewars", "codewars") == "")

    assert (mix("A generation must confront "
                "the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt"
                                                "/1:eee/1:gg/1:ii/1:mm/=:rr")
