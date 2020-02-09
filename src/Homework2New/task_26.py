class MyException(Exception):

    def __init__(self, value, message):
        self._value = value
        self._message = message

    def __str__(self):
        return f'Operation error {self._value}: {self._message}'

    @property
    def _type(self):
        return f'Operation error {self._value}: {self._message}'


def prefix_notation(test_s):
    """Prefix notation

    :param test_s: mathematical expression given as a string in prefix notation
    :return: mathematical expression in infix notation, type: string
    """
    OPERATORS = {'+': float.__add__,
                 '-': float.__sub__,
                 '*': float.__mul__,
                 '/': float.__truediv__,
                 '%': float.__mod__,
                 '^': float.__pow__}
    s = test_s.split()
    temp_stack_str = []
    temp_stack_value = []
    try:

        for char in reversed(s):

            if char not in OPERATORS:
                temp_stack_str.append(char)
                temp_stack_value.append(float(char))

            else:
                x1_str = temp_stack_str.pop()
                x2_str = temp_stack_str.pop()
                x1 = temp_stack_value.pop()
                x2 = temp_stack_value.pop()
                temp_stack_str.append('(' + x1_str + char + x2_str + ')')

                try:
                    temp_result = OPERATORS[char](x1, x2)
                    temp_stack_value.append(temp_result)

                except ZeroDivisionError:
                    return MyException(test_s, 'Division by zero')

        if len(temp_stack_str) != 1:
            return MyException(test_s, 'Wrong format')

        expr = temp_stack_str[0][1:-1]
        return f'Your expression is [ {test_s} ]: {expr} ' \
               f'= {temp_stack_value[0]}'

    except IndexError:
        return MyException(test_s, 'Wrong format')


print(prefix_notation('* +  5 2 + 3 4'))
print(prefix_notation('/ 5 0'))
print(prefix_notation('* * * + 6 7 9 10 2'))
print(prefix_notation('* / * + 6 7 9 10 2'))
print(prefix_notation('* / * +  6 7 9 10 2 4'))
