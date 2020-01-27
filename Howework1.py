# 1---------------------------------------------------------------------------------------------------------------------
print('Hello, world!')
# 2---------------------------------------------------------------------------------------------------------------------
name = input('What is your name?\n')
print('Hi, %s.' % name)
# 3---------------------------------------------------------------------------------------------------------------------
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
# 4---------------------------------------------------------------------------------------------------------------------
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


# 5---------------------------------------------------------------------------------------------------------------------
def greet(names):
    greet('Jack')
    greet('Jill')
    greet('Bob')
    print('Hello' + names)
