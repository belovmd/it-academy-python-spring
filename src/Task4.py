"""4. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

sentence = input("Введите строку: ").replace(" ", "")
result = list(sentence)
answer = list()
for items in result:
    if items not in answer:
        answer.append(items)
print(answer)
