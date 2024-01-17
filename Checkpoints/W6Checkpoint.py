'''
Week 6 Checkpoint: Loans 
'''
# program will ask the user to rate the following information between 1 and 10 to help in the decisioning process:
loan_size = int(input('Rate the size of the loan between 1 - 10: '))
credit_score = int(input('Rate your credit history between 1 - 10: '))
income = int(input('Rate the size of your income between 1 - 10: '))
down_payment = int(input('Rate the size of your down payment between 1 - 10: '))
# will set the "decision" function to be empty until the logic conditions have been met 
decision = None

# Logic portion of the code begins 
if loan_size >= 5: 
    if credit_score >= 7 and income >= 7:
        decision = True 
    elif credit_score >= 7 or income >= 7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False     
else:
    if credit_score < 4:
        decsion = False
    else:
        if income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >= 4:
            decision = True
        else:
            decision = False

# checks the state of the boolean (true or false)
if decision:   
    print('You are approved for the loan!')
else:
    print('Your loan application is denied.')

