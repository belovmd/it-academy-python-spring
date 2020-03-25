"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr).

1. runner() - все функции вызываются по очереди
2. runner('func_name') - вызывается только функция func_name
3. runner('func1', 'func2', ...) - вызывает все переданные функции

2. Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


class Tasks:
    def sort_list(self):
        """Упорядоченный список.

        Дан список целых чисел. Требуется переместить все ненулевые
        элементы в левую часть списка, не меняя их порядок,
        а все нули - в правую часть.
        Порядок ненулевых элементов изменять нельзя,
        дополнительный список использовать нельзя,
        задачу нужно выполнить за один проход по списку.
        Распечатайте полученный список.
        """
        lst = [0, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 3, 4, 5, 0, 2, 3, 0]
        for item in range(len(lst)):
            if lst[item] == 0:
                lst.pop(item)
                lst.append(0)
        print(lst)

    def fibonacci(self):
        """Число Фибоначчи

        Выведите n-ое число Фибоначчи, используя только временные
        переменные, циклические операторы и условные операторы.
        n - вводится
        """
        f_number = s_number = 1
        n = int(input("Enter the n-th Fibonacci number: "))
        while n > 2:
            f_number, s_number = s_number, f_number + s_number
            n -= 1
        print(s_number)

    def symmetric_difference(self):
        """4. Даны два списка чисел.

        Посчитайте, сколько различных чисел входит только в один
        из этих списков
        """
        lst1 = [1, 2, 3, 4, 5, 6, 7, 1, 1, 3, 4, 1, 2, 1, 2, 3, 4, 6]
        lst2 = [2, 3, 4, 3, 4, 5, 8, 4, 5, 7, 2, 1, 2, 3, 2, 3, 5]
        my_set = set(lst1)
        my_set.symmetric_difference_update(set(lst2))
        print("In list {} unique numbers".format(len(my_set)))


def dec(runner):
    def wrapper(*args):
        with open('src/log', 'r+') as f:
            my_count = int(f.read()) + 1
            print("Number of function calls: ", my_count)
            f.seek(0)
            f.write(str(my_count))
        return runner(*args)
    return wrapper


@dec
def runner(*args):
    if len(args) == 0:
        args = [func for func in dir(Tasks) if callable(
                getattr(Tasks, func)) and not func.startswith("__")]
    for elem in args:
        print("Function name: ", elem)
        getattr(tasks, elem)()


tasks = Tasks()
runner()
runner('symmetric_difference')
runner('sort_list', 'symmetric_difference')
