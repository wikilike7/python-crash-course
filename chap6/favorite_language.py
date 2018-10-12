favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('Sarah\'s favorite language is ' + favorite_language['sarah'].title() + '.')

if 'user' not in favorite_language.keys():
    print('Please consider to join our pool')