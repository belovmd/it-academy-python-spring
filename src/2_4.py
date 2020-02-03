""""4. Вводится строка. Требуется удалить из нее повторяющиеся символы
и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""


string = str(input("Insert: "))

new_string = ""

for symbol in string:
    if symbol != " " and symbol not in new_string:
        new_string += symbol

print(new_string)
