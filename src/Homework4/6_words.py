""" Задача 6
Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько различных
слов содержится в этом тексте.

"""


def count_diff_words_in_sentence(text):
    """Return count of different words in input text"""
    return len({word.strip() for word in text.split()})


if __name__ == '__main__':
    test_1 = 'Hello  no      Peter I  am       no am go to    school    Hello'
    assert count_diff_words_in_sentence(test_1) == 8
    test_2 = 'Peter  \t  pls \n  kiss  my dream   \t pls  kiss   my    flower'
    assert count_diff_words_in_sentence(test_2) == 6
