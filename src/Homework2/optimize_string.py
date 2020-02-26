"""String optimization

Function deletes all repeated symbols and whitespaces from input
"""


def optimize_string(string):
    """String optimization.

    Function deletes all repeated symbols and whitespaces from input
    string.

    :param string: input string
    :return: optimized string

    """
    clean_str = ''
    for char in string:
        if char == ' ' or char in clean_str:
            continue
        clean_str += char
    return clean_str


if __name__ == '__main__':
    assert optimize_string('a  ababb c   abc e f') == 'abcef'
