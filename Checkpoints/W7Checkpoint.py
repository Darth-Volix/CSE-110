number = float(input('Please enter a positive number: '))
while number <= 0:
   print('Sorry, that is not a positive number. Please try again.')
   number = float(input('Please enter a positive number: '))

print(f'Thank you! The number is {number}.')

candy = input('May I have a piece of candy?: ')
while candy.lower() != 'yes':
   print('Aww, but I really want one!')
   candy = input('May I have a piece of candy?: ')

print('Thank you! I really like candy.')