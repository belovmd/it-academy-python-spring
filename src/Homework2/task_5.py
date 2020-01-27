def add_binary(a, b):
    """Instructions

    Implement a function that adds two numbers together
    and returns their sum in binary. The conversion can
    be done before, or after the addition.
    The binary number returned should be a string.
    """
    return bin(a + b)[2:]


if __name__ == '__main__':
    a = int(input('Enter 1 number: '))
    b = int(input('Enter 2 number: '))
    print(add_binary(a, b))
