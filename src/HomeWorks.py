def hello_world(self):
    print('Hello, world!')


def hi_name(self):
    name = input('Insert your name:\n')
    print('Hi, %s.' % name)


def friends_list(self):
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print("iteration {iteration} is "
              "{name}".format(iteration=i, name=name))
