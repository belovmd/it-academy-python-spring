"""3. Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

answer = ""
sentence = input("Введите предложение: ").replace(",", "").replace(".", "")\
                                         .replace("?", "").replace("!", "").split(' ')
for words in sentence:
    if len(words) > len(answer):
        answer = words
print(answer)
