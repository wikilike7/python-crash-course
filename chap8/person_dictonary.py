def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name, 'age': age}
    return person


musician = build_person('Shichao', 'Wang', age=20)
print(musician)
