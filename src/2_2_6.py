"""
 One of the simplest ways to hide a secret message
 is to use capital letters. Let's find some of
 these secret messages.

You are given a chunk of text. Gather all capital
letters in one word in the order that they appear
in the text.

For example: text = "How are you? Eh, ok. Low or
Lower? Ohhh.", if we collect all of the capital
letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or
an empty string.

Example:

find_message("How are you? Eh, ok. Low or Lower?
Ohhh.") == "HELLO"
find_message("hello world!") == ""

How it is used: This is a simple exercise
in working with strings: iterate,
recognize and concatenate.

Precondition: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
"""


def find_message(text: str) -> str:
    if 0 < len(text) <= 1000:
        decoded_text = str("")
        for symbol in text:
            if "A" <= symbol <= "Z":
                decoded_text = decoded_text + symbol
        return decoded_text


f = find_message("How are you? "
                 "Eh, ok. Low or Lower? Ohhh.")
print(f)
