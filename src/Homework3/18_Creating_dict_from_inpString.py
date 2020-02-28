"""Create dict from input string

Ввести строку и сделать из нее словарь.
Ключ от значения отделен ': ', пары разделены ', '

"""


def dict_from_string(string):
    """Parse string and create dict"""
    result_dict = dict()
    for dct_item in string.split(', '):
        key, value = dct_item.split(': ')
        result_dict[key] = value
    return result_dict


if __name__ == '__main__':
    inp_string = input('Enter string separating key and value ": "'
                       'and separating pairs by ", ":\n')
    print(dict_from_string(inp_string))
