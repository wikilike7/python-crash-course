alien_0 = {'color': 'green', 'point': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#change the color to red
alien_0['color'] = 'red'

print(alien_0)

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))

# delete key-value pair 
del alien_0['color']
print(alien_0)