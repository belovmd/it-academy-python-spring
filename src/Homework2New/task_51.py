VALUES = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}


def worth_of_words(words):
    """Find word with maximum sum of char's index from VALUES"""

    list_sum = list(map(lambda x: sum(map(lambda y: VALUES[y], x)), words))
    index = list_sum.index(max(list_sum))

    return words[index]


if __name__ == '__main__':

    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(
        ['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")
