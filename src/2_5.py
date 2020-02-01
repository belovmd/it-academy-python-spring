"""5. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы."""


string = str(input("Insert: "))

words = string.split(" ")

new_string = ""
little = big = 0

for element in words:
    new_string += element

for symbol in new_string:
    if "a" <= symbol <= "z":
        little += 1
    elif "A" <= symbol <= "Z":
        big += 1

print("Количество строчных равно {little}, количество прописных {big}".format(little=little, big=big))
