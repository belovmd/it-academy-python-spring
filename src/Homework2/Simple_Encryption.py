"""Simple Encryption #1 - Alternating Split.

For building the encrypted string:
Take every 2nd char from the string, then the other chars,
that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

"""


def decrypt(string, n):
    tmp_list = list()
    for g in range(n):
        for i in range(len(string) // 2):
            tmp_list.append(string[len(string) // 2 + i] + string[i])
        if len(string) % 2 == 1:
            tmp_list.append(string[-1])
        string = ''.join(tmp_list)
        tmp_list.clear()
    return string


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


if __name__ == '__main__':
    assert encrypt("This is a test!", 1) == "hsi  etTi sats!"
    assert decrypt("hsi  etTi sats!", 1) == "This is a test!"
