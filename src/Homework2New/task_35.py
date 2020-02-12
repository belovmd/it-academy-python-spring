VOWELS = "aeiouy"


def translate(phrase):
    """The bird words converter

    - after each consonant letter the bird appends a
    random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of
    the same letter (a ⇒ aaa);
    :param phrase: string
    :return: decodet string
    """

    i = 0
    result_str = ''
    while i <= len(phrase) - 1:
        if phrase[i] in VOWELS:
            result_str += phrase[i]
            i += 3
        elif phrase[i].isalpha():
            result_str += phrase[i]
            i += 2
        else:
            result_str += phrase[i]
            i += 1
    return result_str


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to "
          "review your tests and earn cool rewards!")
