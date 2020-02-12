def checkio(text: str) -> str:
    """The most frequent letter in the text

    The letter returned must be in lower case.
    While checking for the most wanted letter,
    casing does not matter, so for the purpose
    of your search, "A" == "a". Make sure you
    do not count punctuation symbols, digits
    and whitespaces, only letters.
    If you have two or more letters with the same
    frequency, then return the letter which comes
    first in the latin alphabet. For example -- "one"
    contains "o", "n", "e" only once for each, thus we choose "e".
    :param text: string type
    :return: string type
    """

    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    count_dict = dict.fromkeys(alphabet, 0)
    for char in text.lower():
        if char in alphabet:
            count_dict[char] += 1
    return sorted(count_dict, key=lambda x: (-count_dict[x], x))[0]


if __name__ == '__main__':
    checkio('Hello World!')
    print("Example:")
    print(checkio("Hello World!"))
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
