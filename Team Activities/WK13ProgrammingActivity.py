'''
Week 13 Team Activity: Computing Area with Functions
Nicholas Wilkins
12/4/2023
'''
import math 

# Create function to calculate the area of a square 
def compute_area_square(len_side):
    area = len_side ** 2  # This will multiply the len_side by itself
    return area  # returns the result of running the function 

def compute_area_rect(len_side, len_width):
    area = len_side * len_width
    return area 

def compute_area_circle(radius):
    area = math.pi*(radius ** 2) 
    return area

print('\nWelcome to the area calculator!\n')
user_selection = float(input('Please choose an option:\n1. Compute area of a square\n2. Compute area of a rectangle\n3. Compute area of a circle\n4. Quit\nPlease type the number of the option you would like to select: '))
while user_selection != 4:
    if user_selection < 1 or user_selection > 4:
        print('\nI am sorry, that is not an option, please try again!\n')
        user_selection = float(input('Please choose an option!:\n1. Compute area of a square\n2. Compute area of a rectangle\n3. Compute area of a circle\n4. Quit\nPlease type the number of the option you would like to select: '))
    elif user_selection == 1:
        square_side = float(input('Enter the length of the side of a square: '))
        square_area = compute_area_square(square_side)   # passes the value of side into the function, becoming the value of len_side
        print(f'The area of the square is {square_area}\n')
    elif user_selection == 2:
        rect_side = float(input('Enter the length of the side of a rectangle: '))
        rect_width = float(input('Enter the width of a rectangle: '))
        rect_area = compute_area_rect(rect_side, rect_width)
        print(f'The area of the rectangle is {rect_area}\n')
    elif user_selection == 3:
        radius_circle = float(input('Enter the radius of a circle: '))
        circle_area = compute_area_circle(radius_circle)
        print(f'The area of the circle is {circle_area}\n')
    user_selection = float(input('Please choose an option:\n1. Compute area of a square\n2. Compute area of a rectangle\n3. Compute area of a circle\n4. Quit\nPlease type the number of the option you would like to select: '))
print(f'\nThank you, goodbye!\n')