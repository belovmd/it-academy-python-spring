# 3. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке
# -----------------------------------------------------------------------------
sentence = input("Введите предложение:")
sentence = sentence.replace(",", "")
sentence = sentence.replace(";", "")
list_words = sentence.split()

long_word = ""
for word in list_words:
    if len(word) > len(long_word):
        long_word = word

print("Самое длинное слово: " + long_word)
