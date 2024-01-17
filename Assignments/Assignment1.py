print('Hello there! My name is Volix. I would like to get to know you today! I will start by asking a few questions:')

color = input('What is your favorite color? ')   #color is a variable name, input asks the user to input data that becomes the variable "color"
print('Your favorite color is: ',color,'!')      #putting a "," after the string and then adding in the variable will print the string and the variable on the same line
print('I think that is a beautiful color! My favorite color is blue.')

age = input('How old are you? ')                 #repeated technique for practice
print('You are: ',age,"!")
print('You are older than me. My creator made me today, so I am a baby compared to you!')

sport = input('What is your favorite sport? ')   #repeated technique for practice
print('Your favorite sport is: ',sport,'!')
print('I am glad that you have a sport that you enjoy! My creator and I enjoy American Football.')

team = input('What is your favorite team? ')     #repeated technique for practice 
print('Your favorite team is: ',team,'!')
print('Wow, that is so cool! I have no idea whether or not they are good, but my creator tells me he likes the Falcons, who are not very good at the moment.')

print('Here is what I have learned about you:')  #this section of code should complete and summarize everything
print('You are',age,'years-old, you like the color',color,', your favorite sport is',sport,', and your favorite team is',team,'!')

print('I have learned so much about you today, thank you for talking with me. Talk soon!') #Workaround solution so that you can see the program complete before the window closes
exit = input('Press Enter to close program.')
