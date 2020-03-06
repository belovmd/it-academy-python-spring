def checkio(text: str) -> str:
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
