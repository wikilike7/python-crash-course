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