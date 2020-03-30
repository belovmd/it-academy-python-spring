""" Tuple practice tasks

1. Make a tuple from a list ['a', 'b', 'c'].
2. Make a list from a tuple ('a', 'b', 'c').
3. Make the following one line assignments: a = 'a', b=2, c=’python’.
4. Make a tuple with one element. Iterate this tuple in order to print 1, 2, 3.
Make sure that the length of this tuple (len()) is 1.
"""


list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print(type(tuple1), tuple1)


tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print(type(list2), list2)


a, b, c = 'a', 2, 'python'
print("a = {a}, b = {b}, c = {c}".format(a=a, b=b, c=c))


tuple4 = tuple([[1, 2, 3], ], )
print('length = {}'.format(len(tuple4)))
for element in tuple4:
    print(*element)
