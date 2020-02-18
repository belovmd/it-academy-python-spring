""" List practice tasks

1. Use list generator to get the following list:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Use slice to get the following list: ['ab', 'ad', 'bc'].
3. Use list generator to get the following list: ['1a', '2a', '3a', '4a']
4. Use one line solution to get '2a' element and print it.
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
list3 = [str(number) + 'a' for number in range(1, 5)]
print(list3)

# Task 4
print(list3[1])

# Task 5
source_list = ['1a', '2a', '3a', '4a']
target_list = source_list.copy()
target_list.append(source_list.pop(1))
print('target_list = {}, source_list = {}'.format(target_list, source_list))
