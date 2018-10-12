rivers = {
    'yangtze river': 'jiangsu province',
    'yellow river': 'sichuan province',
    'pearl river': 'guangdong province',
}

for message in rivers:
    print('The ' + message.title() + ' runs through ' + rivers[message].title())

for river in rivers.keys():
    print(river.title())

for province in rivers.values():
    print(province.title())