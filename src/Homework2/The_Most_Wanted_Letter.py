"""The Most Wanted Letter.

You are given a text, which contains different english letters and punctuation
symbols. You should find the most frequent letter in the text. The letter
returned must be in lower case. While checking for the most wanted letter,
casing does not matter, so for the purpose of your search, "A" == "a". Make
sure you do not count punctuation symbols, digits and whitespaces, only
letters. If you have two or more letters with the same frequency, then
return the letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each,
thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

("Hello World!") == "l"
("How do you do?") == "o"
("One") == "e"
("Oops!") == "o"

"""
from collections import Counter
import re


def most_freq_letter(text: str) -> str:
    clear_text = ''.join(re.split(r'\W|\d|_', text.lower()))
    count_letters = Counter(clear_text)
    char_count = count_letters.most_common()
    if char_count[0][1] == 1:
        return sorted(clear_text)[0]
    max_count = char_count[0][1]
    tmp_list = [char for char, cnt in char_count if cnt == max_count]
    tmp_list.append(char_count[0][0])
    return sorted(tmp_list)[0]


if __name__ == '__main__':
    assert most_freq_letter("Hello World!") == "l", "Hello test"
    assert most_freq_letter("How do you do?") == "o", "O is most wanted"
    assert most_freq_letter("One") == "e", "All letter only once."
    assert most_freq_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_freq_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_freq_letter("abe") == "a", "The First."
    assert most_freq_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    print('All tests passed!!!')
