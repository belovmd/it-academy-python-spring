"""Find the most popular element in list

Найти самый часто встречающийся элемент списка, состоящего из цифр
(вводится строкой с разделением цифр пробелами).

"""


def most_popular_element(lst):
    """Return the most popular element in list"""
    cnt_elements = dict()
    for item in lst:
        cnt_elements[item] = cnt_elements.get(item, 0) + 1
    return max(cnt_elements.keys(), key=lambda k: cnt_elements[k])


if __name__ == '__main__':
    inp_string = input('Enter numbers separated by whitespaces:\n')
    print(most_popular_element(inp_string.split()))
