age = 122

# if age < 4:
#     print('Your admission cost is $0.')
# elif age < 18:
#     print('Your admission cost is $5.')
# else:
#     print('Your admission cost is $10.')

# # reverse the age
# if age >= 18:
#     print('Your admission cost is $10.')
# elif age >= 4 and age < 18:
#     print('Your admission cost is $5.')
# else:
#     print('Your admission cost is $0.')

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print('Your admission cost is $' + str(price) + '.')