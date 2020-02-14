def checkio(expression):
    """Validator of brackets in expression"""

    bracket_dict = {'(': ')',
                    '[': ']',
                    '{': '}'}
    temp_stack = []
    for char in expression:
        if char in bracket_dict.keys():
            temp_stack.append(char)
        else:
            stack_not_valid = not len(temp_stack)
            if char in ')]}':
                if stack_not_valid or char != bracket_dict[temp_stack.pop()]:
                    return False
    return len(temp_stack) == 0


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)")
    assert checkio("{[(3+1)+2]+}")
    assert not checkio("(3+{1-1)}")
