num1 = float(input('What is the first number?: '))
num2 = float(input('What is the second number?: '))

if num1 > num2:
    print('The first number is greater than the second number.')
else: 
    print('The first number is not greater than the second number.')

if num1 == num2:
    print('The two numbers are equal.')
else:
    print('The two numbers are not equal.')

if num1 < num2:
    print('The second number is greater than the first number.')
else:
    print('The second number is not greater than the first number.')

print()

user_animal = input('What is your favorite animal?: ')

if user_animal.lower == 'Frog':
    print('That is my favorite animal too!')
else:
    print('That is not my favorite.')
