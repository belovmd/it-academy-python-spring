# 5. Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы
# -----------------------------------------------------------------------------
sentence = input("Введите строку:")
upLetter = 0
lowLetter = 0

for letter in sentence:
    if letter.islower():
        lowLetter += 1
    elif letter.isupper():
        upLetter += 1

print("В строке: " + str(lowLetter) + " строчных и " +
      str(upLetter) + " прописных букв")
