"""Caesar Cipher (encryptor).

This mission is the part of the set. Another one - Caesar cipher decriptor.

Your mission is to encrypt a secret message (text only, without special chars
like "!", "&", "?" etc.) using Caesar cipher where each letter of input text
is replaced by another that stands at a fixed distance.
For example ("a b c", 3) == "d e f"

"""


def to_encrypt(text, delta):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_lst = [' ' if char == ' ' else alphabet[
        (alphabet.index(char) + delta) % len(alphabet)]
                for char in text]
    return ''.join(encrypt_lst)


if __name__ == '__main__':
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("ALL TESTS PASSED!!!")
