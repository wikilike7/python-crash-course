pizzas = []
while True:
	topping = input('Enter part: ')
	pizzas.append(topping)
	if topping == 'quit':
		break
	else:
		print(pizzas)
