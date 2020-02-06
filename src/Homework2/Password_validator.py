"""Password validator.

Help develop a password security check module. The password will be
considered strong enough if its length is greater than or equal to
10 symbols, it has at least one digit, as well as containing one uppercase
letter and one lowercase letter in it. The password contains only ASCII
latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be
converted and processed as a boolean.

"""
import re
import unittest


def validate_pass(data: str) -> bool:
    re_pass = r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{10,}$'
    if re.match(re_pass, data):
        return True
    return False


class TestPassValidation(unittest.TestCase):
    def test_pass_validator(self):
        self.assertEqual(validate_pass('A1213pokl'), False)
        self.assertEqual(validate_pass('bAse730onE4'), True)
        self.assertEqual(validate_pass('asasasasasasasaas'), False)
        self.assertEqual(validate_pass('QWERTYqwerty'), False)
        self.assertEqual(validate_pass('123456123456'), False)
        self.assertEqual(validate_pass('QwErTy911poqqqq'), True)


if __name__ == '__main__':
    unittest.main()
