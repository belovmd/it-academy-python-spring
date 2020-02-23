# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

word = input("Enter sentence: ")
list_word = word.replace(',', '').split()
max_word = 0
for index in range(0, len(list_word)):
    if len(list_word[max_word]) < len(list_word[index]):
        max_word = index
print(list_word[max_word])
