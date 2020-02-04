"""Pyramid Slide Down.

For example, let's consider the following problem. Imagine that you
have a pyramid built of numbers, like this one here:

   3
  7 4
 2 4 6
8 5 9 3

Here comes the task...
Let's say that the 'slide down' is a sum of consecutive numbers
from the top to the bottom of the pyramid. As you can see, the
longest 'slide down' is 3 + 7 + 4 + 9 = 23
Your task is to write a function longestSlideDown
(in ruby: longest_slide_down) that takes a pyramid representation as
argument and returns its' longest 'slide down'.

For example,
longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23

By the way...
My tests include some extraordinarily high pyramides so as you can guess,
brute-force method is a bad idea unless you have a few centuries to waste.
You must come up with something more clever than that.

"""
from functools import reduce


def longest_slide_down(pyramid):
    pyr = pyramid[1:]
    while len(pyr) > 1:
        main_list = list()
        tmp_row = list()
        for i_ind, item in enumerate(pyr[0]):
            sum_elements = []
            sum_1 = item + pyr[0 + 1][i_ind]
            sum_2 = item + pyr[0 + 1][i_ind + 1]
            sum_elements.append(sum_1)
            sum_elements.append(sum_2)
            tmp_row.append(sum_elements.copy())
        adv_list = reduce(lambda a, b: a + b, tmp_row)
        main_list.append(adv_list[0])
        for i in range(1, len(adv_list), 2):
            if i == len(adv_list) - 1:
                main_list.append(adv_list[-1])
                break
            else:
                main_list.append(max(adv_list[i], adv_list[i + 1]))
        pyr[1] = main_list.copy()
        pyr = pyr[1:]
        main_list.clear()
    return max(pyr[0]) + pyramid[0][0]


if __name__ == '__main__':
    C = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    L = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    assert longest_slide_down(C) == 23
    assert longest_slide_down(L) == 1074
