def hello_world(self):
    print('Hello, world!')


def hi_name(lst: list):
    name = lst[0]
    surname = lst[1]
    print('Hi, %s %s.' % (name, surname))


def iterable_friends(self):
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print("iteration {iteration} is "
              "{name}".format(iteration=i, name=name))
