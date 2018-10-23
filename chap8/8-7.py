def make_album(singers_name, album_name, number_of_songs=''):
    album_infor = {'singer': singers_name, 'album': album_name}
    if number_of_songs:
        album_infor['song'] = int(number_of_songs)
    return album_infor


while True:
    s_name = input('Enter singer\'s name: ')
    a_name = input('Enter album\'s name: ')
    formatted_name = make_album(s_name, a_name)
    quit_message = input('Do you want to quit(Y/N): ')
    if quit_message == 'y' or 'Y':
        break
    else:
        continue


my_favorite_album = make_album('周杰伦', '七里香')
print(my_favorite_album)

my_favorite_album = make_album('Eason', '白与黑', 30)
print(my_favorite_album)
