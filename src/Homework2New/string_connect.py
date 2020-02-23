# Task - Delete all whitespaces and all duplicate symbols from the string
test_string = input('Enter string: ')
string_without_whitespaces = ''.join(test_string.split())
output_string = ''
for char in string_without_whitespaces:
    if char not in output_string:
        output_string += char
print(output_string)
