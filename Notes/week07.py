'''
Week 7: While loops
Sis Hansen
'''

# while loop to print 'Hello World' 10 times
# we'd usually use a for loop for this (next lesson)
print('Hello World 10 times:')
count = 0
while count < 10:
    print('Hello World!')
    count = count + 1         # could also write as 'count += 1'

 
# while loop dependant on user input 
# print the number the user enters until they input 0
print("\nLet's print your numbers")
user_num = None
while user_num != 0:
    user_num = int(input('Enter a number to print (use 0 to stop): '))
    if user_num != 0:
        print(user_num)
    else:
        print('Program stopped')


# while loop to get user input until it matches 'run' or 'hide'
print("... a scenario from your adventure game ...")
choice1 = None
while choice1 != 'run' and choice1 != 'hide':
    choice1 = input('Enter RUN or HIDE: ')