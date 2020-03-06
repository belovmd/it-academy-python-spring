def checkio(words_set):
    """Suffix and prefix checker

    Check whether there is a pair of words, such that one word is the end
    of another (a suffix of another)
    :param words_set: Words as a set of strings
    :return: True or False
    """
    for suff in words_set:
        for word in words_set:
            if suff != word and word.rfind(suff) == abs(len(word) - len(suff)):
                return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}), "helLO"
    assert not checkio({"hello", "la", "hellow", "cow"}), "hellow la cow"
    assert checkio({"walk", "duckwalk"}), "duck to walk"
    assert not checkio({"one"}), "Only One"
    assert not checkio({"helicopter", "li", "he"}), "Only end"
    print("Done! Time to check!")
