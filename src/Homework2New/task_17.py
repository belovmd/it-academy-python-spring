def rot13(message):
    """Instructions

    ROT13 is a simple letter substitution cipher
    that replaces a letter with the letter 13
    letters after it in the alphabet. ROT13 is
    an example of the Caesar cipher.
    """

    return ''.join(
        [chr(ord(x) + 13 - 26 * ((ord(x) + 12) // 90))
         if x.isupper()
         else
         chr(ord(x) + 13 - 26 * ((ord(x) + 12) // 122))
         if x.islower()
         else x
         for x in message])
