amy_info = {
    'name': 'amy',
    'age': 28,
}

andy_info = {
    'name': 'andy',
    'age': 30,
}

people = [amy_info, andy_info]

for info in people:
    print(info['name'])
    print(info['age'])