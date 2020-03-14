"""Слова
Во входной строке записан текст.
Словом считается последовательность
непробельных символов идущих подряд,
слова разделены одним или большим числом
пробелов или символами конца строки.
Определите, сколько различных слов
содержится в этом тексте.
"""


string = str(input("Insert the string: "))

words_list = string.split()

new_words_list = []

for element in words_list:
    element = element.strip("""`~!@#$%^&*(){}[];:'".,/?<>_""")
    new_words_list.append(element)

dct = {element: new_words_list.count(element) for element in new_words_list}

print(len(dct))
print(dct)
