"""Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
Input: Two arguments. Both are int
Output: Int.
Example:

mult_two(2, 3) == 6
mult_two(1, 0) == 0"""

def mult_two(a: int, b: int) -> int:
    return a * b


f = mult_two(3, 4)
print(f)
