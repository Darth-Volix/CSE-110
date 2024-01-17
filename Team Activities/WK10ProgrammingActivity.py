'''
Week 10 Team Activity: Multiple Lists
Nicholas Wilkins 
11/13/2023
'''
# Sets the variables as empty 
account_name = None
account_balance = None
# Creates empty lists
account_names = []
account_balances = []
# Program begins, asks the user for the names and balances of bank accounts, adding them to their respective lists
print('\nEnter the names and balances of Bank Accounts. Type "quit" when done.')
while account_name != 'quit':
    account_name = input('What is the name of this account?: ')
    if account_name != 'quit':
        account_balance = float(input('What is the balance?: $'))
        account_names.append(account_name)
        account_balances.append(account_balance)
# This section of code will print the account information as was given in the previous section 
print("\nAccount Information:")
for i in range(len(account_names)):
    print(f'{i+1}.', account_names[i], '-', end = ' ')
    print(f'${account_balances[i]:.2f}')
# This section of code will calculate the sum of the account balances and the average balance of the accounts 
balance_total = sum(account_balances)
balance_average = balance_total / len(account_balances)
# Program outputs the total balance and the average balance for the user
print(f'\nTotal Balance: ${balance_total:.2f}\nAverage Balance: ${balance_average:.2f}')
# This section of code searches for the highest account balance, starting by setting the beginning values for new variables
highest_acc_name = None
highest_balance = -1
for i in range(len(account_balances)):
    # The code below sets the variables equal to what is in the list at each index
    highest_name = account_names[i]
    highest_acc_balance = account_balances[i]
    # The code below searches for the highest balance in those lists
    if highest_acc_balance > highest_balance:
        highest_balance = highest_acc_balance
        highest_acc_name = highest_name
# This next line of code will output the name and balance of the account with the highest balance
print(f'Highest Balance: {highest_acc_name} - ${highest_balance}')
# This section creates a while loop that asks the user if they would like to ammend an account balance 
user_input = None
while user_input != 'no':
    print()
    user_input = input('Would you like to update an account? (yes or no): ')
    if user_input.lower() == 'yes':
        change_acc = int(input('What is the account number of the balance you would like to change?: ')) - 1
        change_balance = float(input('What is the new balance for this account?: $'))
        account_balances[change_acc] = change_balance
        print('\nAccount Information:')
        for i in range(len(account_names)):
            print(f'{i+1}.', account_names[i], '-', end = ' ')
            print(f'${account_balances[i]:.2f}')
    elif user_input.lower() != 'yes' or 'no':
        print('I am sorry, that is not an option, please try again!')
print('\nThank you, have a nice day!\n')              