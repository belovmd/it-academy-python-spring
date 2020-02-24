"""Median

A median is a numerical value separating the upper half of a sorted array of
numbers from the lower half. In a list where there are an odd number of
entities, the median is the number found in the middle of the array. If
the array contains an even number of entities, then there is no single
middle value, instead the median becomes the average of the two numbers
found in the middle. For this mission, you are given a non-empty array of
natural numbers (X). With it, you must separate the upper half of the numbers
from the lower half and find the median.

"""
from typing import List


def median(data: List[int]) -> [int, float]:
    data.sort()
    cnt = len(data)
    return data[cnt // 2] if cnt % 2 == 1 else (
        sum(data[cnt // 2 - 1: (cnt // 2) + 1]) / 2)


if __name__ == '__main__':
    assert median([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert median([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert median([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert median([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    assert median(list(range(1000000))) == 499999.5, "Long."
    print("All tests passed!!!")
