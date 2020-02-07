"""Non-unique Elements.

You are given a non-empty list of integers (X). For this task, you should
return a list consisting of only the non-unique elements in this list. To
do so you will need to remove all unique elements (elements which are
contained in a given list only once). When solving this task, do not change
the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements
and result will be [1, 3, 1, 3].

"""


def del_unique(data: list) -> list:
    el_counter = dict()
    for el in data:
        el_counter[el] = el_counter.get(el, 0) + 1
    return [el for el in data if el_counter.get(el) > 1]


if __name__ == "__main__":
    assert list(del_unique([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert list(del_unique([1, 2, 3, 4, 5])) == []
    assert list(del_unique([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(del_unique([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
