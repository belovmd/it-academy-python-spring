# Во входной строке записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.
text = 'Adsds dasda rfs, dfsdf! ASD,df'
for char in text:
    if char.lower() < 'a' or char.lower() > 'z':
        text = text.replace(char, ' ')
set_of_words = set(text.split())
print(len(set_of_words))
