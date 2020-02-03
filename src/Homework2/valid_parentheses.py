"""Valid Parentheses.

Write a function called that takes a string of parentheses,
and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and
false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Along with opening (() and closing ()) parenthesis, input may
contain any valid ASCII characters. Furthermore, the input string
may be empty and/or not contain any parentheses at all. Do not treat
other forms of brackets as parentheses (e.g. [], {}, <>).

"""
import unittest


def valid_parentheses(string):
    opened = closed = 0
    for char in string:
        if closed > opened:
            return False
        if char == '(':
            opened += 1
        elif char == ')':
            closed += 1
    return True if opened == closed else False


class TestValidParentheses(unittest.TestCase):
    def test_parentheses(self):
        self.assertEqual(valid_parentheses("  ("), False)
        self.assertEqual(valid_parentheses(")test"), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi())("), False)
        self.assertEqual(valid_parentheses("hi(hi)()"), True)


if __name__ == "__main__":
    unittest.main()
