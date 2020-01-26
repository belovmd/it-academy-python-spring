import re
test_string = input('Enter string: ')
# The next regular expression splits string with
# all symbols except letters, numbers and _ symbol
list_of_words = re.split(r'\W+', test_string)
flag = True
if list_of_words:
    longest_word = list_of_words[0]
    for word in list_of_words:
        if len(longest_word) < len(word):
            longest_word = word
    for word in list_of_words:
        if len(word) == len(longest_word) and word:
            flag = False
            print(word)
if flag:
    print('There are no words in the string')
