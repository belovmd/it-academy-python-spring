# Task Common price for all items
pr_rubles_per_item = int(input('Enter part of price per item in rubles: '))
pr_cent_per_item = int(input('Enter part of price per item in cents: '))
num_of_items = int(input('Enter numbers of items: '))
common_pr_c = (pr_cent_per_item * num_of_items)
common_pr_r = ((pr_rubles_per_item * num_of_items) + common_pr_c // 100)
print(f'Common price is: {common_pr_r} rubles '
      f'{common_pr_c % 100} cents')
