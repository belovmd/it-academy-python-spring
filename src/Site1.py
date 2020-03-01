# 1) You are given a chunk of text. Gather all capital letters in one word in
# the order that they appear in the text.#
# For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect
# all of the capital letters, we get the message "HELLO".#
# Input: A text as a string (unicode).#
# Output: The secret message as a string or an empty string.


def find_message(text: str) -> str:
    """Find a secret message"""
    message = ""
    for i in range(len(text)):
        if text[i].isupper():
            message += text[i]
    return message


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert find_message(
        "How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool"
        "rewards!")