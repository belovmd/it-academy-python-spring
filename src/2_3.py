"""3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке"""

string = str(input("Insert: "))

new_words = []
words = string.split(" ")
for element in words:
    element = element.strip(".,!?:")
    new_words.append(element)


def sortByLength(new_words):
    return len(new_words)


print(new_words[0])
