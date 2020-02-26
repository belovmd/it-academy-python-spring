# 1.1 Написал бы так
i = 0
while i < 100:
    i += 1
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
# 1.2 Но лучше вот так
i = 0
while i < 100:
    i += 1
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

# 2
f1 = 'ab'
f2 = 'bcd'
lst1 = [i + k for i in f1 for k in f2]
print(lst1)

del lst1[1::2]
print(lst1)

g1 = '1234'
g2 = 'a'
lst2 = [i + k for i in g1 for k in g2]
print(lst2)

lst2.remove('2a')
print(lst2)

lst2.extend(lst2.copy())
lst2.append('2a')
print(lst2)

# 3
a1 = list('abc')
b1 = tuple('abc')
print(b1)

c1 = tuple('abc')
d1 = list('abc')
print(d1)

a, b, c = 'a', 2, 'python'

f = [1, 2, 3],
e = tuple(f)
print(e, len(e))
