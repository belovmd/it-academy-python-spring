try:
    price_rubles_per_item = int(input('Enter part of price per item in rubles: '))
    price_cent_per_item = int(input('Enter part of price per item in cents: '))
    numbers_of_items = int(input('Enter numbers of items: '))
    common_price_cents = (price_cent_per_item * numbers_of_items)
    common_price_rubles = ((price_rubles_per_item * numbers_of_items)
                           + common_price_cents // 100)
    print(f'Common price is: {common_price_rubles} rubles '
          f'{common_price_cents % 100} cents')
except ValueError as error:
    print(error)
