# Найти самое длинное слово в введенном предложении. Учтите что в
# предложении есть знаки препинания.

text = str(input("Enter text "))
for ch in [',', '.', '!', '?']:
    if ch in text:
        text = text.replace(ch, '')
words = text.split()
maxlen = words[0]
for i in range(1, len(words)):
    if len(words[i]) > len(words[i - 1]):
        maxlen = words[i]
print(maxlen)
