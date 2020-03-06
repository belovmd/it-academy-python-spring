def to_camel_case(name):
    """CamelCase formatter

    Convert the name of a function (a string) from the
    Python format (for example "my_function_name") into CamelCase
    ("MyFunctionName"), where the first char of every word is in uppercase
    and all words are concatenated without any intervening characters.
    :param name: A function name as a string
    :return: The same string, but in CamelCase
    """
    new_string = ''
    for index, char in enumerate(name):
        if index == 0:
            new_string += char.upper()
        elif name[index - 1] == '_':
            new_string += char.upper()
        elif char != '_':
            new_string += char
    return new_string


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
