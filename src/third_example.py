# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
from string import punctuation


word = input("Enter sentence: ")
list_word = word.replace(',', '').split()
max_word = ''
for word in list_word:
    word = word.strip(punctuation)
    if len(word) > len(max_word):
        max_word = word
print(max_word)

