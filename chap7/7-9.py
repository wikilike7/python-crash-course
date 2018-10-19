sandwich_orders = ['The caprese', 'Clam roll', 'pastrami', 'Ham and cheese', 'The Jibarito', 'pastrami', 'Bologna sandwich', 'pastrami']

print('The pastrami is sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
