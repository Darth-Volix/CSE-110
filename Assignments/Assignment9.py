'''
Weeks 9 & 10 Assigment: Shopping Cart
Nicholas Wilkins
11/08/2023
'''

print('\nWelcome to the Shopping Cart Program!\n')

# Establishes that the user input, shopping cart, and cost cart exist but are empty.
user_input = None
shopping_cart = []
cost_cart = []

while user_input != 6:
    # This section prints the option menu.
    print('Please select one of the following options:')
    print('1. Add Item')
    print('2. View Cart')
    print('3. Remove Item')
    print('4. Compute Total')
    print('5. Compute Total W/Tax')
    print('6. Quit')
    # Program now asks user which option they would like to select.
    user_input = int(input('Please type the number of the action you would like to take: '))

    if user_input == 1: 
        # User selected they would like to add and item to the shopping cart, this section of code asks for the item and adds it.
        user_item = input('What item would you like to add to the shopping cart?: ')
        item_cost = float(input('How much does the item cost?: $'))
        shopping_cart.append(user_item)
        cost_cart.append(item_cost)
        print(f'\n"{user_item}" has been added to the shopping cart.\n')
    elif user_input == 2:
        # User selected that they would like to see the contents of the shopping cart. Program prints list of items.
        print('\nThe contents of the shopping cart are:')
        for i in range(len(shopping_cart)):
            print(f'{i+1}.', shopping_cart[i], end = '')
            print(f' ${cost_cart[i]}')  
        print()
    elif user_input == 3:
        # User selected that they would like to remove an item. 
        print('\nThe contents of the shopping cart are:')
        for i in range(len(shopping_cart)):
            print(f'{i+1}.', shopping_cart[i], end = '')
            print(f' ${cost_cart[i]}')  
        print()
        user_remove = int(input('What item number would you like to remove?: ')) - 1
        removed_item = shopping_cart.pop(user_remove)
        removed_cost = cost_cart.pop(user_remove)
        print(f'\n"{removed_item}", which cost ${removed_cost}, was removed from your cart.\n')
    elif user_input == 4: 
        # User selected that they would like to compute the subtotal. 
        total_cart_cost = sum(cost_cart)
        print(f'\nThe total cost of the items in the shopping cart is ${total_cart_cost:.2f}!\n')
    elif user_input == 5:
        # User selected that they would like to compute the total with tax.
        total_cart_cost = sum(cost_cart)
        tax = float(input('What is the tax rate in your area? (answer in 0.00 format with only two decimals): '))
        tax_rate = (tax / 100) + 1
        total_tax = (tax /100) * total_cart_cost
        total_with_tax = total_cart_cost * tax_rate
        print(f'\nThe cart subtotal is ${total_cart_cost:.2f} with ${total_tax:.2f} in tax for a total price of ${total_with_tax:.2f}!\n')
    elif user_input == 6:
        # User selected that they would like to quit the program.
        print('\nThank you. Goodbye.\n')
    else:
        # User typed in a number that was not an option. 
        print('I am sorry, that is not one of the available options. Please try again. \n')


