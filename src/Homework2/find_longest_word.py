import re
import unittest


def find_longest_word_in_sentence(sentence):
    """Function finds the longest word in sentence."""
    all_words_list = re.split(r'\W', sentence)
    longest_word = sorted(all_words_list,
                          key=lambda item: len(item),
                          reverse=True)[0]
    return longest_word


class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        sentence = ('Yes, Google is ***the most&^ great !corporation!!!'
                    '!!! your+ @email is not >passed :validation;;')
        self.assertEqual(find_longest_word_in_sentence(sentence),
                         'corporation')


if __name__ == '__main__':
    unittest.main()
