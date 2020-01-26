try:
    var = int(input('Enter the number: '))
    var_test = var // 10
    number_order = 0
    while var_test > 0:
        number_order += 1
        var_test //= 10
    for power in range((number_order // 2) + 1):
        left_num = (var // 10 ** (number_order - power)) % 10
        right_num = (var % (10 ** (power + 1))) // (10 ** power)
        if left_num != right_num:
            print("It's not polindrom")
            break
    else:
        print('Polindrom')
except ValueError as error:
    print(error)
