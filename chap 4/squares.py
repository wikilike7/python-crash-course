# method 1
squares = []
for value in range(0, 11):
    squares.append(2** value)
print(squares)

# method 2
another_squares = [2** value for value in range(0, 11)]
print(another_squares)