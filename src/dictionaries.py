prices = {'apple': 0.40, 'banana': 0.80}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(my_purchase[fruit]*prices[fruit]
                   for fruit in my_purchase)
print('I-ve owe the grocer $%.2f' % grocery_bill)
