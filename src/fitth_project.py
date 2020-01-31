# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

words = input("Enter: ")
new_words = words.replace(' ', '')
counter_upper = 0
counter_lower = 0
for index in new_words:
    if 'A' <= index <= 'Z':
        counter_upper += 1
    elif 'a' <= index <= 'z':
        counter_lower += 1
print("quantity upper words: ", counter_upper)
print("quantity lower words: ", counter_lower)