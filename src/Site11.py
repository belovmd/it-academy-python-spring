# 11) The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter
# (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
# You are given an ornithological phrase as several words which are separated
# by white-spaces (each pair of words by one whitespace). The bird does not
# know how to punctuate its phrases and only speaks words as letters. All words
# are given in lowercase. You should translate this phrase from the bird
# language to something more understandable.
VOWELS = "aeiouy "


def translate(phrase):
    phrase = list(phrase)

    # Find index of glasn after sogl
    index_of_glasn = [i + 1 for i in range(len(phrase)) if phrase[i] not in
                      VOWELS]

    # Adding chars with index not in index_of_glasn in new phrase
    new_phrase = [phrase[i] for i in range(len(phrase)) if i not in
                  index_of_glasn]
    new_phrase = ''.join(new_phrase)
    for char in VOWELS:
        if new_phrase.find(char * 3) >= 0:
            new_phrase = new_phrase.replace(char * 3, char)
    return new_phrase


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool "
          "rewards!")
