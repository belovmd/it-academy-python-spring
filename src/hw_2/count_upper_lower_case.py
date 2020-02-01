""" Calculate the number of lower case and upper case letters in a string. Take
into consideration only english letters.
"""


string = input()
ord_a = ord('a')
ord_z = ord('z')
ord_upper_a = ord('A')
ord_upper_z = ord('Z')
lower_case_count = 0
upper_case_count = 0
for char in string:
    code = ord(char)
    if ord_a <= code <= ord_z:
        lower_case_count += 1
    if ord_upper_a <= code <= ord_upper_z:
        upper_case_count += 1
print(f"Upper case english letters number is: {upper_case_count}, "
      f"lower case english letters number is: {lower_case_count}.")
