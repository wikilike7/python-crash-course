users = ['admin', 'andy', 'bob', 'kevin', 'lucas']
# users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?' )
        else:
            print('Hello ' + user + ', thank you for logging in again.')
else:
    print('We need some users')

# 5.10
current_users = ['a', 'b', 'c', 'd', 'e']
new_users = ['A', 'b', 'x', 'y', 'z']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Used')
    else:
        print('New')

# 5.11
# 将数字和数字的序号一一对应
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
ordinal_number = 0

for number in numbers:
    print(str(number) + ' ---> ' + str(ordinal_numbers[ordinal_number]))
    ordinal_number += 1