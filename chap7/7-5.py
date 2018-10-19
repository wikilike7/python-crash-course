while True:
	age = int(input('How years old of you?'))
	if age < 3:
		print('Your can go film free')
		break
	elif age <= 12:
		print('Your film price is 10$')
		break
	else:
		print('Your film price is 15$')
		break
