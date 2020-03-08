"""
Sort Array by Element Frequency: Moderate

Sort the given iterable so that its elements
end up in the decreasing frequency order,
that is, the number of times they appear in
elements. If two elements have the same
frequency, they should end up in the same
order as the first appearance in the iterable.

Input: Iterable
Output: Iterable
Precondition: elements can be ints or strings
"""


def frequency_sort(items):
    dct_items = {element: items.count(element)
                 for element in items}
    dct_items_sorted = {key: value for key, value
                        in sorted(dct_items.items(),
                                  key=lambda x: x[1],
                                  reverse=True)}
    lst = [element for element in dct_items_sorted
           for _ in range(dct_items_sorted.get(element))]
    return lst


print(frequency_sort([4, 6, 2, 2, 6, 4, 2, 4, 4]))
