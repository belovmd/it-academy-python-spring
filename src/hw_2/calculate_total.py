"""Calculate total price in roubles and penny.

Input:
    M - rouble
    N - penny
    L - amount
Output: total sum.
"""

print("Input roubles, penny, amount:")
roubles, penny, amount = map(int, input().split())

total_roubles = roubles * amount + penny * amount // 100
total_penny = (penny * amount) % 100

print(f"Total: {total_roubles} roubles and {total_penny} penny.")
