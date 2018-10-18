cities = {
    'Oslo': {
        'country': 'Norway',
        'Population': '615,000',
        'Alias': 'Kristiania'
    },
    'Reykjavik': {
        'Country': 'Iceland',
        'Population': '115,000',
        'Alias': 'Smoked Gulf Coast'
    },
    'Stockholm': {
        'Country': 'Sweden',
        'Population': '806,000',
        'Alias': 'Northern Venice'
    },
}

for city, info in cities:
    print(city + ': ')
    print(info)
