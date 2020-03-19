"""Во входной строке записан текст. Словом считается последовательность

непробельных символов идущих подряд, слова разделены одним или большим числом

пробелов или символами конца строки. Определите, сколько различных слов

содержится в этом тексте.

"""

words = "My name   is Andrei  name  Sarha Thank  Andrei you\nfriend \tOh La La"
word = words.lower().split()
counter = 0
start = 0
for elem in word:
    start += 1
    for index in range(start, len(word)):
        if elem == word[index]:
            counter += 1
counter *= 2
result = len(word) - counter
print(result)
