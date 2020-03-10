"""Complete the function scramble(str1, str2) that returns true
if a portion of str1 characters can be rearranged to match str2,
otherwise returns false.

Notes:
    Only lower case letters will be used (a-z). No punctuation
    or digits will be included.
    Performance needs to be considered

Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

Sample Tests:
Test.assert_equals(scramble('rkqodlw', 'world'), True)
Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
Test.assert_equals(scramble('katas', 'steak'), False)
Test.assert_equals(scramble('scriptjava', 'javascript'), True)
Test.assert_equals(scramble('scriptingjava', 'javascript'), True)
"""


def scramble(s1, s2):
    count = 0
    for elem in s2:
        if elem in s1 and s2.count(elem) <= s1.count(elem):
            count += 1
    if count == len(s2):
        return True
    else:
        return False
