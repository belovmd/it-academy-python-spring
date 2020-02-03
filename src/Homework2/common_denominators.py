"""Common denominators.

You will have a list of rationals in the form:
[ [numer_1, denom_1] , ... [numer_n, denom_n] ]

where all numbers are positive ints.

You have to produce a result in the form:
[ [N_1, D] ... [N_n, D] ]

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

"""
from functools import reduce


def simple_num_list(n):
    lst = [i for i in range(n + 1)]
    simple_num = list()
    for k in range(2, n + 1):
        if lst[k]:
            simple_num.append(lst[k])
            for m in range(k ** 2, n + 1, k):
                if lst[m]:
                    lst[m] = 0
    return simple_num


def calc_NOK(l):
    full = []
    for i in l[1][:]:
        if i in l[0]:
            full.append(i)
            l[0].remove(i)
            l[1].remove(i)
    full += l[0] + l[1]
    for i in l[2:]:
        for n in i:
            if (n not in full) or i.count(n) > full.count(n):
                full.append(n)
    return reduce(lambda a, b: a * b, full)


def NOK(l):
    if sum(l) / len(l) == l[0]:
        return int(l[0])
    l.sort(reverse=True)
    simple_nums = simple_num_list(l[0])
    glob_delitel = []
    delitel = []
    for num in l:
        for simple_num in simple_nums:
            if num == 1:
                break
            while num % simple_num == 0:
                delitel.append(simple_num)
                num /= simple_num
        if delitel:
            glob_delitel.append(delitel[:])
            delitel.clear()
    nok = calc_NOK(glob_delitel)
    return nok


def convertFracts(lst):
    if lst:
        all_elem = list()
        for inner_struct in lst:
            all_elem.append(inner_struct[1])
        inner_list = []
        outer_list = []
        nok = NOK(all_elem)
        for inner_struct in lst:
            inner_list.append(int(nok / inner_struct[1]) * inner_struct[0])
            inner_list.append(nok)
            outer_list.append(inner_list[:])
            inner_list.clear()
        return outer_list
    return lst


if __name__ == '__main__':
    test_array = [
        [[1, 2], [1, 3], [1, 4]],
        [[69, 130], [87, 1310], [3, 4]],
        [[1, 1], [3, 1], [4, 1], [5, 1]],
    ]

    result_array = [
        [[6, 12], [4, 12], [3, 12]],
        [[18078, 34060], [2262, 34060], [25545, 34060]],
        [[1, 1], [3, 1], [4, 1], [5, 1]],
    ]

    for i in range(3):
        assert convertFracts(test_array[i]) == result_array[i]
