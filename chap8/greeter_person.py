def get_formatted(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('Please tell me your name:')
    # print('Press "q" to quit')
    f_name = input('Fist Name: ')
    l_name = input('Last Name: ')
    formatted_name = get_formatted(f_name, l_name)
    print('Hello, ' + formatted_name)
    exit_prompt = input('Press "q" to quit the program: ')
    if exit_prompt == 'q':
        break
