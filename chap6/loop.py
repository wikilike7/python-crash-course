favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# use sorted 
for name in sorted(favorite_languages):
    print(name.title() + ', thank you for taking the poll.')

# print the value of elements
for value in favorite_languages.values():
    print('The value is: ' + value.title())

# remove the duplicates
for language in set(favorite_languages.values()):
    print(language.title())
