"""Most frequently used words in a text.

Write a function that, given a string of text (possibly with punctuation
and line-breaks), returns an array of the top-3 most occurring words, in
descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more
apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be
lowercased. Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or
top-1 words should be returned, or an empty array if a text contains no words.

Examples:
top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]

"""
from collections import Counter
import re
import unittest


def top_3_words(text):
    print(text)
    words = re.split(r'[-,.! &@#$?;_:/\\]', text.lower())
    words_count = Counter(words)
    lst = [word.strip("-") for word, count in
           sorted(words_count.items(),
                  key=lambda i: i[1], reverse=True) if re.search(r'\w', word)]
    return lst[:3]


class TestTopWords(unittest.TestCase):
    def test_top_3_words(self):
        self.assertEqual(top_3_words(" //wont won't won't"), ["won't", "wont"])

        test_str = ("uaAnDzXB,uaAnDzXB!?pnLGMyLn.!-uaAnDzXB pnLGMyLn:_"
                    "/uaAnDzXB .uaAnDzXB,_..;pnLGMyLn;uaAnDzXB;:,/pnLGMyLn!. "
                    "uaAnDzXB  ;;/pnLGMyLn.uaAnDzXB;,!_pnLGMyLn "
                    "/uaAnDzXB:--pnLGMyLn?--pnLGMyLn..?uaAnDzXB,?_; "
                    "uaAnDzXB: !,!pnLGMyLn:")
        self.assertEqual(top_3_words(test_str), ['uaandzxb', 'pnlgmyln'])


if __name__ == '__main__':
    unittest.main()
