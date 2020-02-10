string=input('введите строку: ').split()
count=0
for i in string:
    if len(i)>count:
        count=len(i)
        word=i
print('самое длинное слово: ',word)