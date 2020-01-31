# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

words = input("Enter sentence: ")
list_words = words.replace(',', '').split()
max_word = 0
for index in range(0, len(list_words)):
    if len(list_words[max_word]) < len(list_words[index]):
        max_word = index
print(list_words[max_word])
