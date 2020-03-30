""" List practice tasks

1. Use list generator to get the following list:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Use slice to get the following list: ['ab', 'ad', 'bc'].
3. Use list generator to get the following list: ['1a', '2a', '3a', '4a']
4. Use one line solution to delete '2a' element and print it.
5. Copy list and add element '2a'. After this operation the source list
shouldn't have this element.
"""


# Task 1
list1 = [char1 + char2 for char1 in 'ab' for char2 in 'bcd']
print(list1)


# Task 2
list2 = list1[::2]
print(list2)


# Task 3
list3 = [number + 'a' for number in '1234']
print(list3)


# Task 4
print(list3.pop(1))


# Task 5
list4 = list3.copy()
list4.append('2a')
print('target_list = {}, source_list = {}'.format(list4, list3))
