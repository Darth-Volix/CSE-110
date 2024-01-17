'''
Week 10 Checkpoint
Nicholas Wilkins 
11/13/2023
'''

user_input = None
item_list = []
print('\nWhat item would you like to add to this list? (type "quit" to finish):')
while user_input != 'quit':
    user_input = input('Item: ')
    if user_input != 'quit':
        item_list.append(user_input)

print('\nThe Shopping List is:')
for i in range(len(item_list)):
    print(item_list[i])

print('\nThe shopping list with indexes is:')
for i in range(len(item_list)):
    print(f'{i}.', item_list[i])

change_item = int(input('What item number would you like to change?: '))
new_item = input("What item would you like to add in it's place?: ")
item_list[change_item] = new_item

print('\nThe new item list is:')
for i in range(len(item_list)):
    print(f'{i}.', item_list[i])