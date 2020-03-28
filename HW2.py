# for №2.6
from bs4 import BeautifulSoup
import requests
# for №3
import string


# 1 --------------------------------------------------
MN = input("Введите цену:")
MN = float(MN.replace(",", "."))
L = int(input("Введите количество:"))
total = MN * L
MN_RUB = int(total)
MN_PEN = int((total - int(total)) * 100)
print("Общая цена {} рублей {} копеек".format(MN_RUB, MN_PEN))


# 2.1 ------------------------------------------------
"""You are given a positive integer. Your function should calculate the
product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be
1*2*3*4*5=120 (don't forget to exclude zeroes).
Input: A positive integer.
Output: The product of the digits as an integer."""


def digits_mult(number: int):
    result = 1
    for s in str(number):
        res = int(s)
        if res != 0:
            result *= res
    print(result)


digits_mult(123405)
digits_mult(999)
digits_mult(1000)
digits_mult(1111)


# 2.2 ------------------------------------------------
"""You are given a chunk of text. Gather all capital letters in one word
in the order that they appear in the text.
For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we
collect all of the capital letters, we get the message "HELLO".
Input: A text as a string (unicode).
Output: The secret message as a string or an empty string."""


def find_message(text: str):
    cap = ''
    for x in text:
        if x.isupper():
            cap += x
    print(cap)


find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
find_message("hello world!")
find_message("HELLO WORLD!!!")


# 2.3 ------------------------------------------------
"""You are given an array of integers. You should find the sum of the integers
with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the
final element of the array together. Don't forget that the first element has
an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer."""


def even_the_last(array):
    result = 0
    if not array:
        print(result)
    else:
        for f in range(0, len(array), 2):
            result += array[f]
        print(result * array[-1])


even_the_last([0, 1, 2, 3, 4, 5])
even_the_last([1, 3, 5])
even_the_last([6])
even_the_last([])


# 2.4 ------------------------------------------------
"""You are given the current stock prices. You have to find out which stocks
cost more.
Input: The dictionary where the market identifier code is a key and the value
is a stock price.
Output: The market identifier code (ticker symbol) as a string."""


def best_stock(data):
    max_price = 0
    answer = ''
    for key in data:
        if data[key] > max_price:
            max_price = data[key]
            answer = key
        elif data[key] == max_price:
            print(key)
    print(answer)


best_stock({"CAC": 390.2, "ATX": 390.2, "WIG": 1.2})
best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9})


# 2.5 ------------------------------------------------
"""You are given two strings and you have to find an index of the second
occurrence of the second string in the first one.
Let's go through the first example where you need to find the second
occurrence of "s" in a word "sims". It’s easy to find its first occurrence
with a function index or find which will point out that "s" is the first
symbol in a word "sims" and therefore the index of the first occurrence is 0.
But we have to find the second "s" which is 4th in a row and that means that
the index of the second occurrence (and the answer to a question) is 3.
Input: Two strings.
Output: Int or None"""


def second_index(text: str, symbol: str):
    if text.count(symbol) < 2:
        print(None)
    else:
        first = text.find(symbol)
        print(text.find(symbol, first + 1))


second_index("sims", "s")
second_index("find the river", "e")
second_index("hi", " ")
second_index("hi mayor", " ")
second_index("hi mr Mayor", " ")


# 2.6 ------------------------------------------------
"""Parser EUR from nbrb.by"""

url = 'https://www.nbrb.by/statistics/rates/ratesdaily.asp'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class': 'currencyTable'})
tr = table.findAll('td', {'class': 'curCours'})
tr = tr[5].text
print('Курс Евро: ', tr)


# 3 --------------------------------------------------
my_str = input()
my_punc = str.maketrans(dict.fromkeys(string.punctuation))
my_word = my_str.translate(my_punc).split()
my_word.sort(key=len)
print(my_word[-1])


# 4 --------------------------------------------------
string = input()
string_n = ''
for i in range(len(string)):
    if string_n.find(string[i]) == -1 and string[i] != ' ':
        string_n += string[i]
print(string_n)


# 5 --------------------------------------------------
my_str = input()
catalog = {}
for let in my_str:
    if 'a' <= let <= 'z' or 'A' <= let <= 'Z':
        if let in catalog:
            catalog[let] = catalog[let] + 1
        else:
            catalog[let] = 1
for k in catalog:
    print(k, ':', catalog[k])


# 6 --------------------------------------------------
# n-th Fibonacci number
fib1 = fib2 = 1
n = int(input())
if n < 2:
    quit()
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')


# 6 --------------------------------------------------
# Palindrome (True or False)
num_pal = input()
rev_num_pal = num_pal[::-1]
if num_pal == rev_num_pal:
    print('True')
else:
    print('False')
