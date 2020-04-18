"""1 - Runner
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""
import types

import funcs_for_task_1


def runner(*args):
    """Run all funcs from module or only passed to the function args"""
    amount_result = []

    def run(funcs):
        for func in funcs:
            if hasattr(funcs_for_task_1, func):
                f_res = getattr(funcs_for_task_1, func)()
                if isinstance(f_res, types.GeneratorType):
                    amount_result.append(next(f_res))
                else:
                    amount_result.append(f_res)
    if args:
        funcs = args
    else:
        funcs = [attr for attr in funcs_for_task_1.__dict__ if not (
            attr.startswith('__')
        ) and callable(getattr(funcs_for_task_1, attr))]
    run(funcs)
    return amount_result


if __name__ == '__main__':
    assert runner() == ['func_1', 'func_2', 'func_3', 'gen_1']
    assert runner('func_1', 'gen_1') == ['func_1', 'gen_1']
    assert runner('func_3') == ['func_3']
