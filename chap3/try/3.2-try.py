# 3.4
guests = ['Frod Baggins', 'Gandoff', 'Edolas']
print('I want to invite ' + guests[0] + ', ' + guests[1] + ' and '+ guests[2] + ' to join the party.')

# 3.5, modify the guest list
del guests[0]
print(guests[0] + ' can not join us, so we will invite another one')
guests.insert(0, 'Rivendell')
print(guests)
print('I want to invite ' + guests[0] + ', ' + guests[1] + ' and '+ guests[2] + ' to join the party.')

# 3.6, add guests
print('I find a bigger table!')
guests.insert(0, 'Samwise Gamgee')
print(guests)
guests.insert(2, 'Merry')
print(guests)
guests.append('Pip')
print(guests)
print('I want to invite ' + str(guests))

# 3.7
print('Sorry, i can only invite two guests to join the party')
print('Hi ' + guests.pop() + ', i can not invite you.')
print('Hi ' + guests.pop() + ', i can not invite you.')
print('Hi ' + guests.pop() + ', i can not invite you.')
print('Hi ' + guests.pop() + ', i can not invite you.')
# print('Hi ' + guests.pop() + ', i can not invite you.')
# print('Hi ' + guests.pop() + ', i can not invite you.')
print(guests)
print(guests[1] + ', i always invite you')
print(guests[0] + ', i always invite you')
guests.remove('Rivendell')
print(guests)
guests.remove('Samwise Gamgee')
print(guests)