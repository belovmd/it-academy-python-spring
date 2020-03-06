def checkio(text: str) -> str:

    """You are given a text, which contains different english letters

    and punctuation symbols. You should find the most frequent

    letter in the text. The letter returned must be in lower case.

    While checking for the most wanted letter, casing does not matter,

    so for the purpose of your search, "A" == "a". Make sure you do not count

    punctuation symbols, digits and whitespaces, only letters.

    If you have two or more letters with the same frequency,

    then return the letter which comes first in the latin alphabet.

    For example -- "one" contains "o", "n", "e" only once for each,

    thus we choose "e".

    Input: A text for analysis as a string.

    Output: The most frequent letter in lower case as a string.
    """

    max_count = 0
    lower_registor = text.lower()
    max_word = text[0]
    for element in lower_registor:
        if element.isalpha():
            if lower_registor.count(element) > max_count:
                max_word = element
                max_count = lower_registor.count(element)
            elif lower_registor.count(element) == max_count:
                if element < max_word:
                    max_word = element
                    max_count = lower_registor.count(element)
    return max_word


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and
    # not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
