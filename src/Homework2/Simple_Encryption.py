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


def decrypt(s, n):
    l = []
    for g in range(n):
        for i in range(len(s) // 2):
            l.append(s[len(s) // 2 + i] + s[i])
        if len(s) % 2 == 1:
            l.append(s[-1])
        s = ''.join(l)
        l.clear()
    return s


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


if __name__ == '__main__':
    assert encrypt("This is a test!", 1) == "hsi  etTi sats!"
    assert decrypt("hsi  etTi sats!", 1) == "This is a test!"
