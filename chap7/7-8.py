sandwich_orders = ['French dip', 'Egg salad', 'The Dagwood']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print('I made ' + sandwich_order + ' sandwich')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for sandwich_order in finished_sandwiches:
    print(sandwich_order)

