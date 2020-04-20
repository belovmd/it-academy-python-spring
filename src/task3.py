# Реализовать функцию get_ranges которая получает на вход непустой список
# неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
# список “сворачивает”


def get_ranges(lst):
    intervals = []
    intervals_str = ''
    i = 0
    for el in lst:
        if not intervals or intervals[i][1] + 1 != el:
            intervals.append([el, el])
            i = len(intervals) - 1
        else:
            intervals[i][1] += 1
    for el in intervals:
        if len(set(el)) == 1:
            intervals_str += '{}, '.format(el[0])
        else:
            intervals_str += '{} - {}, '.format(el[0], el[1])
    return intervals_str.rstrip(', ')


print(get_ranges([1, 2, 3, 7, 8, 10]))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9, 10]))
