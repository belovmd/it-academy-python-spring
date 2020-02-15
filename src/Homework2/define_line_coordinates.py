"""ДЗ из лекции 13-02-20

Уравнение прямой вида y = kx + b задано в виде строки. Решить уравнение с
заданным x.
Данные вводятся в таком виде: 2x + 1

"""


def solve_equation(str_equation, x):
    equation = list(map(lambda s: s.strip(), str_equation.split()))
    for el in equation:
        if 'x' in el:
            var_k = int(el.replace('x', ''))
        elif el in '-+':
            operator = el
        else:
            var_b = int(el)
    return var_k * x + var_b if operator == '+' else var_k * x - var_b


if __name__ == '__main__':
    solve_equation('2x - 3', 3) == 3
    solve_equation('3 + 2x', 2) == 7
    print('All tests passed!!!')
