#  Вводится строка. Требуется удалить из нее повторяющиеся символы и все
#  пробелы. Например, если было введено "abc cde def", то должно быть выведено
#  "abcdef".

text = 'abc cde de'
newtext = ''.join(text.split())
obrnewtext = newtext[::-1]
for char in newtext:
    kol = obrnewtext.count(char)
    if kol > 1:
        obrnewtext = obrnewtext.replace(char, '', kol - 1)
print(obrnewtext[::-1])
