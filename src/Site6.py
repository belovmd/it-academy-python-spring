# 6) Sort the given iterable so that its elements end up in the decreasing
# frequency order, that is, the number of times they appear in elements.
# If two elements have the same frequency, they should end up in the same
# order as the first appearance in the iterable.


def frequency_sort(items):
    n = len(set(items))
    count_of_items = {}
    for el in items:
        count_of_items[el] = count_of_items.get(el, 0) + 1

    def f(e):
        return count_of_items[e]
    items.sort(key=f, reverse=True)
    for times in range(n):
        first_el = items[0]
        for el in items:
            if el == first_el:
                items.remove(el)
                items.append(el)
    return items


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4,
                                                              4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
