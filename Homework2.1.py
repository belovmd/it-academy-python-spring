M = int(input('Рубли: '))
N = int(input('Копейки: '))
L = int(input('Колличество: '))
M1 = M * L + N * L // 100
N1 = (N * L) % 100
print('Общая цена ' + str(M1) + ' Рублей ' + str(N1) + ' Копеек')
