# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
# часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
lst = [2, 3, 0, 1]
for el in lst:
    if el == 0:
        lst.remove(el)
        lst.append(0)
print(lst)
