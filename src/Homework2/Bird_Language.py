"""Bird Language.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter
(l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

Example:

translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"

"""
import re


VOWELS = "aeiouy"


def translate(phrase):
    words = phrase.split(' ')
    for i, word in enumerate(words[:]):
        b_ch = re.findall(r'[qwrtpsdfghjklzxcvbnm][aeiouy]|[aeiouy]{3}', word)
        words[i] = ''.join([char[0] for char in b_ch])
    return ' '.join(words)


if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Mission complete!!!")
