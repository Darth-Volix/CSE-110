'''
Week 7 Team Activity: Magic Number
Nicholas Wilkins
10/23/2023
'''

import random

play_again = 'yes'

while play_again.lower() == 'yes':
    magic_number = random.randint(1,100)
    guess_number = 0
    guess = int(input('What is the magic number?: '))
    while guess != magic_number:
        if guess < magic_number:
            guess_number = guess_number + 1
            print('Sorry, that is not the magic number. The magic number is higher than your guess.')
            guess = int(input('What is the magic number?: '))
        elif guess > magic_number:
            guess_number = guess_number + 1
            print('Sorry, that is not the magic number. The magic number is lower than your guess.')
            guess = int(input('What is the magic number?: '))
    guess_number = guess_number + 1
    print(f'You guessed it! It took you {guess_number} tries!')
    play_again = input('Would you like to play again?: ')
print('Thank you for playing, goodbye!')

    