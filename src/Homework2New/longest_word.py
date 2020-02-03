test_string = input('Enter string: ')
punckt = """" ,.?!/()*{}[]:;"'"""

list_of_words = []

for word in test_string.split():
    list_of_words.append(word.strip(punckt))

max_len = len(max(list_of_words, key=len))

for word in list_of_words:
    if len(word) == max_len:
        print(word)
