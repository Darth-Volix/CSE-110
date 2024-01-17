'''  
Team Activity: Grade Calculator
'''

grade_percentage = float(input('What is is your grade percentage in the class?: '))

if grade_percentage >= 90:
    grade = 'A'
elif grade_percentage < 90 and grade_percentage >= 80:
    grade = 'B'
elif grade_percentage < 80 and grade_percentage >= 70:
    grade = 'C'
elif grade_percentage < 70 and grade_percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

sign = ''
last_digit = grade_percentage % 10

if last_digit >= 7:
    sign = '+'
elif last_digit < 4:
    sign = "-"
else:
    sign = ''

if grade_percentage >= 94 or grade_percentage < 60:
    sign = ''

print(f'Congratulations, you got a {grade}{sign}!')

if grade_percentage <= 70:
    print('You get to take this class again you newb!')
else:
    print('You get to move on to the next class!')