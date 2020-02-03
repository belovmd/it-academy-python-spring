st = input('Vvedite stroku:')
newst = ""
for i in st:
    if i not in newst and i != " ":
        newst += i
print(newst)
