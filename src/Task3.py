"""3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

answer = ""
sentence = input("Введите предложение: ")
sentence = "".join(elem for elem in sentence
                   if elem.isalpha() or elem == " ").split()
for words in sentence:
    if len(words) > len(answer):
        answer = words
print(answer)
