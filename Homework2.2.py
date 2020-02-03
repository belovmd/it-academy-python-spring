sentence = input('Введите предложение: ')
changed_sentence = sentence.replace(",", "")
changed_sentence = sentence.replace("!", "")
changed_sentence = sentence.replace("?", "")
changed_sentence = sentence.replace(".", "")
list_words = changed_sentence.split()
longest_word = 0
for i in range(1, len(list_words)):
    if len(list_words[longest_word]) < len(list_words[i]):
        longest_word = i
print(list_words[longest_word])
