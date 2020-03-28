# Даны два натуральных числа. Вычислите их наибольший общий делитель при
# помощи алгоритма Евклида (мы не знаем функции и рекурсию).


def nod(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.
def quantity(lst1, lst2):
    common_num = set(lst1).intersection(set(lst2))
    return 'Quantity of common numbers = {}'.format(len(common_num))


# Во входной строке записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.
def different_words(text):
    for char in text:
        if char.lower() < 'a' or char.lower() > 'z':
            text = text.replace(char, ' ')
    set_of_words = set(text.split())
    return len(set_of_words)
