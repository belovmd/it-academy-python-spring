def find_outlier(integers):
    """Instructions

    [2, 4, 0, 100, 4, 11, 2602, 36]
    Should return: 11 (the only odd number)
    [160, 3, 1719, 19, 11, 13, -21]
    Should return: 160 (the only even number)
    """
    odd = 0
    even = 0
    for number in integers:
        if number % 2 == 0:
            odd += 1
            odd_num = number
        else:
            even += 1
            even_num = number
        if odd == 1 and even > 1:
            return odd_num
        if even == 1 and odd > 1:
            return even_num
