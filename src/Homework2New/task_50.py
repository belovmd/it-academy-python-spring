import re


def check_pangram(text):
    """Pangram checker

    :param text: string
    :return: bool
    """

    text = ''.join(re.split(r'\W+', text.replace('_', '')))
    return len(set(text.lower())) == 26


if __name__ == '__main__':

    assert check_pangram("The quick brown fox jumps over the lazy dog.")
    assert not check_pangram("ABCDEF")
    assert check_pangram("Bored? Craving a pub quiz fix? Why, "
                         "just come to the Royal Oak!")
