"""
Determine if a number is a palindrome. Without using of strings.
Input: a number.
Output "Yes" if a palindrome, "No" if not.
"""

number = int(input())
temp = number
reverted_number = 0
while temp > 0:
    reverted_number = reverted_number * 10 + temp % 10
    temp = temp // 10
if number == reverted_number:
    print("Yes")
else:
    print("No")
