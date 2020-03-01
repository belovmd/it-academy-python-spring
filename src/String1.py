# Найти самое длинное слово в введенном предложении. Учтите что в
# предложении есть знаки препинания.

text = '(Hello, Wo!}:*/+-'
new_text = ''
max_lenth = ''
for char in text:
    if 'a' <= char.lower() <= 'z' or char == ' ':
        new_text += char
text = new_text.split()
for word in text:
    if len(word) > len(max_lenth):
        max_lenth = word
print(max_lenth)
