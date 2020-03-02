""" Calculate the number of lower case and upper case letters in a string. Take
into consideration only english letters.
"""


string = input()
lower_case_count = 0
upper_case_count = 0
for char in string:
    if 'a' <= char <= 'z':
        lower_case_count += 1
    if 'A' <= char <= 'Z':
        upper_case_count += 1
print('Upper case english letters number is:', upper_case_count)
print('Lower case english letters number is:', lower_case_count)
