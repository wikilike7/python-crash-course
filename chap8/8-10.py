magicians = ['Dynamo', 'Jason Latimer', 'Franz Harary']
temp_magicians = []


def show_magicians(name):
    for i in name:
        print(i)


def make_great(current_name):
    # j = len(current_name)
    while current_name:
        # j = current_name.pop()
        temp_magicians.append('The great ' + current_name.pop())
        # temp_magicians = sorted(temp_magicians)
    print(temp_magicians)


make_great(magicians)
show_magicians(magicians)


