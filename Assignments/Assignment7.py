'''
Week 7 and 8 Assignment: Wordle
Nicholas Wilkins
11/04/2023
'''
import random 

play_again = 'yes'

while play_again.lower() == 'yes':
    # list of possible words
    words = ['temple', 'mosiah', 'nephi', 'lehi', 'mormon', 'ammon']   
    # selects a word at random from the list 
    win = random.choice(words)   
    # sets the guess count to 1 in case the user gets it right the first time
    guess_count = 1    
    print()
    print('Welcome to the word guessing game!')
    print()
    # This next line of code will enable it so that "your hint is" has the hint underscores print on the same line
    print('Your hint is: ', end = ' ')
    for i in range(len(win)):
        print('_', end = ' ')
    # Program will ask user for an input on what the secret word is
    print() 
    print()
    guess = input('What is the secret word?: ')
    while guess.lower() != win:
        # adds one to guess count since the user got it wrong
        guess_count = guess_count + 1  
        print()  
        # This next line of code will check if the user input is the same length as the win word
        if len(guess) != len(win):
            print(f'Your guess was not the same length as the word. The word has {len(win)} letters. Please try again.')
        else: 
            print('I am sorry, that is not the secret word!')
            print()
            print('Your hint is: ', end = ' ')
            for i in range(len(guess)) and range(len(win)):
                if guess[i] == win[i]:
                    print(guess[i].upper(), end = ' ')
                elif guess[i] in win:
                    print(guess[i].lower(), end = ' ')
                else:
                    print('_', end = ' ')
        print()
        print()
        guess = input('What is the secret word?: ')
    # user guessed the word correctly
    print()
    print(f'Congratulations, you found the secret word! Total number of guesses was {guess_count}.')
    print() 
    play_again = input('Would you like to play again?: ')
    print()
# user did not want to play again
print()
print('Thank you for playing. Have a nice day!') 
print()
