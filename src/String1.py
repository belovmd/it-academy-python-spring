# Найти самое длинное слово в введенном предложении. Учтите что в
# предложении есть знаки препинания.

text = input("Enter text ")
punkt = '.,!? ()'
words = text.split()
maxlen = ''
for i in words:
    if len(i.strip(punkt)) > len(maxlen):
        maxlen = i.strip(punkt)
print(maxlen)
