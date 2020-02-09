"""Secret Message

You are given a chunk of text. Gather all capital letters in one word in the
order that they appear in the text. For example: text = "How are you? Eh, ok.
Low or Lower? Ohhh.", if we collect all of the capital letters, we get the
message "HELLO".

Example:
find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""

"""


def find_message(text: str) -> str:
    return ''.join([char for char in text if char.isupper()])


if __name__ == '__main__':
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_message("hello world!") == ""
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD"
    print('Done!')
