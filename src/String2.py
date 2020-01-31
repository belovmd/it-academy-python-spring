# Посчитать количество строчных (маленьких) и прописных (больших) букв в
# введенной строке. Учитывать только английские буквы.

text = str(input("Enter text "))
small = 0
big = 0
for i in text:
    if 'a' <= i <= 'z':
        small += 1
    elif 'A' <= i <= 'Z':
        big += 1
print("Number of small = ", small, "\nNamber of big = ", big)
