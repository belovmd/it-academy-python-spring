"""This time no story, no theory. The examples below show you
how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters
from a..z and A..Z.

Sample Tests:
Test.describe("accum")
Test.it("Basic tests")
Test.assert_equals(accum("ZpglN"), "Z-Pp-Ggg-Llll-Nnnnn")
Test.assert_equals(accum("Nyffs"), "N-Yy-Fff-Ffff-Sssss")
Test.assert_equals(accum("MjtkU"), "M-Jj-Ttt-Kkkk-Uuuuu")
Test.assert_equals(accum("Evidj"), "E-Vv-Iii-Dddd-Jjjjj")
Test.assert_equals(accum("Hbide"), "H-Bb-Iii-Dddd-Eeeee")
"""


def accum(s):
    a = ""
    for elem in range(len(s)):
        a += (((elem + 1) * s[elem]) + "-").capitalize()
    return a[:-1]
