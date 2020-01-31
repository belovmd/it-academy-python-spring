# Вводится строка. Требуется удалить
# из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

word = input("Enter sentence: ")
new_word = ""
for index in word:
    if index not in new_word and index != '':
        new_word += index
print(new_word.replace(" ", ""))
