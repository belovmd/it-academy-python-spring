# You are given the current stock prices.
# You have to find out which stocks cost more.


def best_stock(a):
    biggest = 0
    for i in a:
        if a[i] > biggest:
            biggest = a[i]
    for stock, price in a.items():
        if price == biggest:
            return stock


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
