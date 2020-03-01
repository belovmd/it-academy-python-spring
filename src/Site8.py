# 8) You are given an expression with numbers, brackets and operators. For
# this task only the brackets matter. Brackets come in three flavors: "{}" "()"
# or "[]". Brackets are used to determine scope or to restrict some expression.
# If a bracket is open, then it must be closed with a closing bracket of the
# same type. The scope of a bracket must not intersected by another bracket.
# In this task you should make a decision, whether to correct an expression
# or not based on the brackets. Do not worry about operators and operands.


def checkio(expression):
    brackets = '(){}[]'
    for char in expression:
        if char not in brackets:
            expression = expression.replace(char, '')

    for j in range(len(expression)):
        if '()' in expression:
            pos = expression.find('()')
            expression = expression[:pos] + expression[pos + 2:]
        elif '{}' in expression:
            pos = expression.find('{}')
            expression = expression[:pos] + expression[pos + 2:]
        elif '[]' in expression:
            pos = expression.find('[]')
            expression = expression[:pos] + expression[pos + 2:]
    if len(expression) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") is True, "Simple"
    assert checkio("{[(3+1)+2]+}") is True, "Different types"
    assert checkio("(3+{1-1)}") is False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") is True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") is False, "One is redundant"
    assert checkio("2+3") is True, "No brackets, no problem"
