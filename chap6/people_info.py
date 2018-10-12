# 6.1

people_info = {
    'first_name': 'shichao',
    'last_name': 'wang',
    'age': '21',
    'city': 'nanjing'
}

for person in people_info:
    print(person.title() + ': ' + people_info[person].title())

# 6.2

favorite_numbers = {
    'zibba': '13',
    'Andy': '1',
    'Amy': '2',
}

for favorite_number in favorite_numbers:
    print(favorite_number.title() + '\'s favorite number is ' + favorite_numbers[favorite_number].title())

#  6.3

vocabularys = {
    'variable': 'present a placehoder or container to fill in data',
    'Array': 'an orded data set',
    'Tuple': 'same with Array but can\'t changed',
    'Data type': 'present what kind of the data, like integer, string, float',
    'condition statement': 'if condition',
}

for vocabulary in vocabularys:
    print(vocabulary.title() + ': ' + vocabularys[vocabulary].title())