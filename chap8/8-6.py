def city_country(city, country):
    return '\n' + city + ', ' + country


b_c, r_i, b_u = city_country('Beijing', 'China'), city_country('Reykjavik', 'Iceland'), city_country('Boston', 'USA')
print(b_c, r_i, b_u)
