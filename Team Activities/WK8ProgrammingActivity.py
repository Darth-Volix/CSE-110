'''
Week 8 Team Activity
Nicholas Wilkins
10/30/2023
'''

marriage = 'commitment'
user_letter = input('What letter should be capitalized?: ')
for i in range(len(marriage)):                # len assigns an integer to each letter in the variable
    if marriage[i] == user_letter:
      print('_', end = ' ')                   # end = ' ' makes it so the program does not start a new line after each letter
    else:
      print(marriage[i], end = ' ')           