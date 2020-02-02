RUBLES = int(input('Please, enter part of price per item in rubles: '))
CENTS = int(input('Please, enter part of price per item in cents: '))
count = int(input('Please, enter count of product: '))
total_rubles = RUBLES * count + (CENTS * count) // 100
total_cents = (CENTS * count) % 100
print(f'Total price {total_rubles} rubles '
      f'{total_cents} cents')
