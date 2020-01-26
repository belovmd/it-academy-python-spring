def sum_numbers_recursion(number):
    """Instructions (with conversion num to string)

    A digital root is the recursive sum of all
    the digits in a number. Given n, take the
    sum of the digits of n. If that value has
    more than one digit, continue reducing in
    this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    """
    if number < 10:
        return number
    sum_num = sum(map(int, str(number)))
    return sum_numbers_recursion(sum_num)


def sum_numbers_recursion_2(number):
    """Instructions (without conversion num to list  )

    A digital root is the recursive sum of all
    the digits in a number. Given n, take the
    sum of the digits of n. If that value has
    more than one digit, continue reducing in
    this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    """
    if number < 10:
        return number
    var_test = number // 10
    number_order = 0
    sum_num = 0
    while var_test:
        number_order += 1
        var_test //= 10
    for power in range(number_order + 1):
        left_num = (number // 10 ** (number_order - power)) % 10
        print(left_num, end='')
        if power < number_order:
            print('+', end='')
        sum_num += left_num
    print()
    if sum_num >= 10:
        print(sum_num)
    return sum_numbers_recursion_2(sum_num)


if __name__ == '__main__':
    var = int(input('Enter the number: '))
    print(sum_numbers_recursion_2(var))
    print(sum_numbers_recursion(var))
