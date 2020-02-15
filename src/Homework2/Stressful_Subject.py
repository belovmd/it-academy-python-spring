"""Stressful Subject

The function should recognise if a subject line is stressful. A stressful
subject line means that all letters are in uppercase, and/or ends by at
least 3 exclamation marks, and/or contains at least one of the following
“red” words: "help", "asap", "urgent". Any of those "red" words can be
spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other
letters interspersed between them.

Input: Subject line as a string.
Output: Boolean.
Example:
is_stressful("Hi") == False
is_stressful("I neeed HELP") == True

"""
import re


def is_stressful(subj):
    """recognize stressful subject"""
    if subj[len(subj) - 3:] == '!!!':
        return True
    if subj.isupper():
        return True
    words_list = subj.lower().split()
    for word in words_list:
        if re.search(
                r'(?=.*?h)(?=.*?e)(?=.*?l)(?=.*?p).'
                r'|(?=.*?a)(?=.*?s)(?=.*?a)(?=.*?p).'
                r'|(?=.*?u)(?=.*?r)(?=.*?g)(?=.*?e)'
                r'(?=.*?n)(?=.*?t).', word):
            return True
    return False


if __name__ == '__main__':
    # These "asserts" are only for auto-testing
    assert not is_stressful("Hi")
    assert is_stressful("I neeed HELP")
    assert is_stressful("HI HOW ARE YOU?")
    assert is_stressful("This is very urgent!")
    assert is_stressful("U-R-G-E-N-T issue")
    assert is_stressful("UUUURGGGEEEEENT here")
    assert is_stressful("where are you?!!!!")
    assert is_stressful("We need you A.S.A.P.!!")
    print('Done! Go Check it!')
