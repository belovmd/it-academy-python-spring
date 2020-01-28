# 1
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed (Just like the name of this Kata). Strings passed
# in will consist of only letters and spaces. Spaces will be included
# only when more than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"
def spinWords(stroka):
    list_stroka = stroka.split()
    for i, word in enumerate(list_stroka):
        if len(word) >= 5:
            list_stroka[i] = word[-1::-1]

    return " ".join(list_stroka)


# -----------------------------------------------------------------------------
# 2
# Disarium number is the number that The sum of its digits powered
# with their respective positions is equal to the number itself.
#   175
# 1      7      5
# 1**1 + 7**2 + 5**3
# 1    + 49   + 125
#   175
#   175 == 175  - Disarium !
def disarium_number(number):
    disarium = 0
    i = 1
    for digital in str(number):
        disarium += int(digital) ** i
        i += 1

    if number == disarium:
        return "Disarium!"
    else:
        return "No disarium"


# -----------------------------------------------------------------------------
# 3
# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
#   i increments the value (initially 0)
#   d decrements the value
#   s squares the value
#   o outputs the value into the return array
#   Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]
def parse(data):
    out_list = [0]
    index_list = 0
    n_str = 0
    for letter in data:
        if letter == 'i':
            out_list[index_list] += 1
        elif letter == 'd':
            out_list[index_list] -= 1
        elif letter == 's':
            out_list[index_list] = out_list[index_list] ** 2
        elif letter == 'o':
            if n_str < len(data) - 1:
                out_list.append(out_list[index_list])
            index_list += 1
        n_str += 1
    return out_list


# -----------------------------------------------------------------------------
# 4
# Write a function that takes in a binary string and returns
# the equivalent decoded text (the text is ASCII encoded).
#
# Each 8 bits on the binary string represent 1 character on the ASCII table.
#
# The input string will always be a valid binary string.
#
# Characters can be in the range from "00000000" to "11111111" (inclusive)
#
# Note: In the case of an empty binary string your function should
#         return an empty string.
def binary_to_string(binary):
    stroka = ""
    index = 0
    while index < len(binary):
        stroka += chr(int(binary[index:index + 8], 2))
        index += 8  # go bytes
    return stroka


# -----------------------------------------------------------------------------
# 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples
# of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    sum_multiple = 0
    for i in range(1, number):
        if i % 3 == 0:
            sum_multiple += i
        elif i % 5 == 0:
            sum_multiple += i
    return sum_multiple

# -----------------------------------------------------------------------------
# 1
# print(spinWords( "Hey fellow warriors" ))
# print(spinWords( "This is a test"))
# print(spinWords( "This is another test" ))

# 2
# print(disarium_number(89))
# print(disarium_number(518))
# print(disarium_number(1024))
# print(disarium_number(175))
# print(disarium_number(25))

# 3
# print(parse("iiisdoso")) # [8, 64]
# print(parse("ooo"))    # [0,0,0])
# print(parse("ioioio")) # [1,2,3])
# print(parse("idoiido")) # [0,1])
# print(parse("isoisoiso")) # [1,4,25])
# print(parse("codewars"))

# 4
# print(binary_to_string('0100100001100101011011000110110001101111'))  # 'Hello'
# print(binary_to_string('00110001001100000011000100110001'))  # '1011'

# 5
# print(solution(10))
