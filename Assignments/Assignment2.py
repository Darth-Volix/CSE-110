'''
Week 2 Assignment: Word Games
Nicholas Wilkins 
09/23/2023
'''
# Importing the time library so that I can have some fun making it seem like the computer is working hard :)
import time  

# Writing the program to seem like the program has a personality, also practicing using \n 
print()
print('Hello there! This is Volix, your friendly computer program! \nI would like to write a madlib for you. \nPlease enter the following information:')
print()

# Program begins to ask the user for information to make the madlib
noun = input('A Noun: ')
place = input('A Place: ')
verb = input('A Verb ending in "ing": ')
exclamation = input('An Exclamation (such as "What on earth?!"): ')
adjective = input('An Adjective: ')
noun2 = input('Another Noun: ')
name = input('A Name: ')
print()
time.sleep(0.5)
print('Thank you for providing me with that information! Please allow me a few moments to process.')
time.sleep(2)

# This section of code will output the madlib using the input the user has given
print()
print('Here is your madlib:')
print()
print(f'I was walking down the street when I saw a giant {noun} in front of the {place}. \nIt was {verb} and making a loud noise. "{exclamation.title()}!" I exclaimed as I ran away. \nAs I was running, I bumped into someone else. I apologized and looked at their face. \nTo my surprise, they had a {noun2} on their forehead! They said their name was {name.title()} and that they were from another planet. \nThey told me to follow them if I wanted to escape the giant {noun}. I had no other choice, so I followed them to safety. \nI hope I never see aliens or a giant {noun} again!')
print()