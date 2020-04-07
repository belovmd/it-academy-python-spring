"""Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только
функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все
переданные функции """


class HomeWorks:
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


def runner(*func):
    for element in func:
        getattr(HomeWorks(), element, "Task is not chosen")()

    if not func:
        for element in HomeWorks.__dict__:
            attr = ['__module__', '__dict__',
                    '__weakref__', '__doc__']
            if str(element) not in attr:
                getattr(HomeWorks(), element, "Task is not chosen")()


runner('hello_world', 'friends_list')
