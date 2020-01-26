import re
test_string = input('Enter string: ')
# lower_chars = upper_chars = 0
# for char in test_string:
#     if char.islower():
#         lower_chars += 1
#     if char.isupper():
#         upper_chars += 1
# print(f'Numbers of lower chars is: {lower_chars}')
# print(f'Numbers of upper chars is: {upper_chars}')
lower_chars = len(re.findall(r'[a-z]', test_string))
upper_chars = len(re.findall(r'[A-Z]', test_string))
print(f'Numbers of english lower chars is: {lower_chars}')
print(f'Numbers of english upper chars is: {upper_chars}')
