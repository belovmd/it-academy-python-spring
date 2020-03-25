def nod(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def quantity(lst1, lst2):
    common_num = set(lst1).intersection(set(lst2))
    return 'Quantity of common numbers = {}'.format(len(common_num))


def different_words(text):
    for char in text:
        if char.lower() < 'a' or char.lower() > 'z':
            text = text.replace(char, ' ')
    set_of_words = set(text.split())
    return len(set_of_words)
