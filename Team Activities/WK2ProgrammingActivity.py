'''
Week 2: Programming Activity
Nicholas Wilkins
09/18/2023
'''

print('Please enter the following information: ')

print()                                             # adds a space between the question and the inputs for requested information 

First = input('What is your first name? ')
Last = input('What is your last name? ')
Email = input('What is your email address? ')       # Lines 10-16 asks the user for the information to create their ID
Phone = input('What is your phone number? ')
Job = input('What is your Job Title? ')
ID_Number = input('What is your ID Number? ') 
ID_Number = int(ID_Number)                          # Converts the string value of the variable into an integer 

print()                                             # adds a space between the question and the inputs for the requested information

print('The ID Card is:')
print('-'*30)                                       # This will print "-" 30 times
print(f'{Last.upper()}, {First.lower()}')           # The .upper function makes everything upper case, the .lower function does the opposite
print(Job.title())                                  # The .title function ensures that the first letter of the names will be uppercase
print(f'ID: {ID_Number}')                           # Lines 19 - 27 will output the actual ID card 
print()
print(Email)
print(Phone)
print('-'*30)







