def build_person(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    print(full_name)


build_person('shichao', 'wang')
build_person('shichao', 'wang', '123')
