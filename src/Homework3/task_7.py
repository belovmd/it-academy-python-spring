def chocolate(n=1, m=1, k=1, t=1):
    """Cutting chocolate

    res1: if numbers of cutting pieces less than total chocolate pieces,
    and n or m is divider of k, then True

    res2: single pieces can be cutting just from side, so True
    if k = n or k = m and m != 1 or n != 1.
    Also we can cut single pieces from one-line chocolate if k < (n or m)

    res3: if k >= total chocolate pieces or number of cuts more
    than max possible number of cuts n * m - 1 then return False
    else find minimum numbers of cuts to get k single pieces of chocolate
    if minimum numbers of cuts <= t then return True
    minimum numbers of cuts with choose between 3 results:
        result 1 : if n is divider of k then k // n
        result 2 : if m is divider of k then k // m
        result 3 : calculate numbers of whole lines of longest side
                   of chocolate whole_slices = k // max(n, m):
                       if reminder of choc. after cuts whole lines = 1 line or
                        k % (longest side) = shortest line - whole lines
                        then add 1 to whole lines value
                        else add 2 to whole lines value
    """
    res_1 = (k % n == 0 or k % m == 0) and k < n * m
    res_2 = k == n and m != 1 or k == m and n != 1 \
        or k < n and m == 1 or k < m and n == 1

    # res_3
    max_nmb_of_cutting = n * m - 1
    min_nmb_1 = min_nmb_2 = min_nmb_3 = max_nmb_of_cutting

    if k >= n * m or t > max_nmb_of_cutting:
        return res_1, res_2, False

    if k % n == 0:
        min_nmb_1 = k // n
    elif k % m == 0:
        min_nmb_2 = k // m
    else:
        whole_slices = k // max(n, m)
        if min(n, m) - whole_slices == 1 or \
                k % max(n, m) == min(n, m) - whole_slices:
            min_nmb_3 = whole_slices + 1
        else:
            min_nmb_3 = whole_slices + 2

    return res_1, res_2, min(min_nmb_1, min_nmb_2, min_nmb_3) <= t


assert chocolate(2, 1, 2, 1) == (False, False, False)
assert chocolate(3, 6, 8, 2) == (False, False, True)
assert chocolate(3, 6, 9, 3) == (True, False, True)
assert chocolate(3, 6, 9, 12) == (True, False, True)
assert chocolate(3, 6, 9, 2) == (True, False, False)
assert chocolate(6, 3, 18, 1) == (False, False, False)
assert chocolate(6, 6, 6, 2) == (True, True, True)
assert chocolate(5, 6, 29, 5) == (False, False, True)
