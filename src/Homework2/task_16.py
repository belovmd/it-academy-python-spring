from collections import Counter


def anagrams(word, words):
    """Instructions

    'abba' & 'baab' == true
    'abba' & 'bbaa' == true
    'abba' & 'abbba' == false
    'abba' & 'abca' == false
    """
    counts = Counter(word)
    return [word_in for word_in in words if counts == Counter(word_in)] or []


if __name__ == '__main__':
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa',
                             'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers',
                              'racer']) == ['carer', 'racer']
