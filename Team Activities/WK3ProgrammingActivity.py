import math

square_length = float(input('What is the length of the side of a square? '))
print(f'The area of the square is {square_length*square_length}')

rect_length = float(input('What is the length of the side of a rectangle? '))
rect_width = float(input('What is the length of the width of a rectangle? '))
print(f'The area of the rectangle is {rect_length*rect_width}')

rad_circle = float(input('What is the radius of a circle? '))
print(f'The area of the cirlce is {math.pi*rad_circle**2}')