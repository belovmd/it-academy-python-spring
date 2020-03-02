""" https://py.checkio.org/mission/stressful-subject/solve/

The function should recognise if a subject line is stressful. A stressful
subject line means that
    1) all letters are in uppercase,
    2) and/or ends by at least 3 exclamation marks,
    3) and/or contains at least one of the following “red” words:
"help", "asap", "urgent". Any of those "red" words can be
spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other
letters interspersed between them.

Input: Subject line as a string.
Output: Boolean.
Precondition: Subject can be up to 100 letters
"""


def replace_multiple_chars(char, word):
    while char * 2 in word:
        word = word.replace(char * 2, char)
    return word


def is_stressful(sentence):
    result = False
    if sentence.isupper() or sentence[-3:] == '!!!':
        result = True
    else:
        sentence = sentence.lower().replace(
            '-', '').replace('!', '').replace('.', '')

        stress_words = ["help", "asap", "urgent"]
        stress_letters = set("".join(stress_words))

        words = sentence.split()
        for word in words:
            if word[0] in ('h', 'a', 'u'):
                for char in stress_letters:
                    word = replace_multiple_chars(char, word)
                if word in stress_words:
                    result = True
            if result:
                break
    return result


if __name__ == '__main__':
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    assert is_stressful("i NEED a break ") is False
    assert is_stressful("I don't need help anymore") is True

    assert is_stressful("H!E!L!p i need somebody ...") is True
    assert is_stressful("not just anyboooody heeeelp") is True
    assert is_stressful("you know I need somewones h-eeeeeel-p!") is True

    assert is_stressful("I need your bike and clothes...") is False
    assert is_stressful("A.S.A.P") is True

    print('Done! Go Check it!')
