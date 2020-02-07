"""Sort Array by Element Frequency.

Sort the given iterable so that its elements end up in the decreasing
frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same
order as the first appearance in the iterable.

sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]

"""
from collections import Counter


def frequency_sort(items):
    cnt = Counter(items)
    if not items or cnt.most_common(1)[0][1] == 1:
        return items
    return [k for k, n in cnt.most_common() for _ in range(n)]


if __name__ == '__main__':
    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert frequency_sort([17, 99, 42]) == [17, 99, 42]
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]
