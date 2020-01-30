# M = int(input('Рубли: '))
# N = int(input('Копейки: '))
# L = int(input('Колличество: '))
# M1 = M * L + N * L // 100
# N1 = (N * L) % 100
# print('Общая цена ' + str(M1) + ' Рублей ' + str(N1) + ' Копеек')


# sentence = input('Введите предложение: ')
# changed_sentence = sentence.replace(",", "")
# changed_sentence = sentence.replace("!", "")
# changed_sentence = sentence.replace("?", "")
# changed_sentence = sentence.replace(".", "")
# list_words = changed_sentence.split()
# longest_word = 0
# for i in range(1, len(list_words)):
#     if len(list_words[longest_word]) < len(list_words[i]):
#         longest_word = i
# print(list_words[longest_word])


# st = input('Vvedite stroku:')
# newst=""
# for i in st:
#     if i not in newst and i !=" ":
#         newst += i
# print(newst)


# s = input()
# let_s = 0
# let_b = 0
# for i in s:
#     if 'a' <= i <= 'z':
#         let_s += 1
#     else:
#         if 'A' <= i <= 'Z':
#             let_b += 1
# print(let_s)
# print(let_b)


# def mult_two(a, b):
#     return a * b

# def say_hi(name: str, age: int) -> str:
#     name = "Alex"
#     age = 32
#     return "Hi. My name is "+name+" and I'm "+str(age)+" years old"


# def easy_unpack(elements):
#     return elements[0],elements[2],elements[-2]

# def index_power(array: list, n: int):
#     if len(array) <= n:
#         return -1
#     else:
#         return array[n]**n