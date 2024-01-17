'''
Week 3 & 4 Assignment: Meal Cost Calculator
Nick Wilkins 
10/04/2023
'''
import time         #Importing time library so that I can use it to make it seem like the computer has to think about the calculations :)

print()
print('Hello there! This is Volix, your friendly computer program. \nSounds like you need some help calculating the cost of a meal!')
print()
print('Please enter the following information: ')
print()

kids_meal = float(input("What is the price of a kid's meal?: $"))                             #Code begins asking user for meal cost info
adult_meal = float(input('What is the price of a meal for an adult?: $'))
kids = int(input('How many kids are there?: '))
adults = int(input('How many adults are there?: '))
base_tax = float(input('What is the sales tax rate? (enter in format X.XX without a "%" sign): '))
tip_rate = float(input('What percentage of the meal cost do you plan on tipping? (enter in format XX.XX without a "%" sign): '))
meal_cost = float((kids_meal*kids)+(adult_meal*adults))                  #Calculates the total cost of meal pre-tax
total_tip = float(meal_cost*((tip_rate/100)))                            #Calculates tip amount
tax_rate_multiplier = float((base_tax/100)+1)                            #Converts tax rate to number we can multiply meal cost by to get the total cost of the meal (including tax)
tax_rate = float(base_tax/100)                                           #Converts tax rate to number we can use to get the total sales tax
print()
print('Thank you for that information! Allow me a moment to process.')
print()

time.sleep(1)                        #Fun time delay :)

print(f'Meal Cost: ${meal_cost:.2f}')                                           #Outputs total cost before tip and tax
print(f'Tip: ${total_tip:.2f}')                                                 #Outputs total tip
print(f'Meal Subtotal: ${(meal_cost+total_tip):.2f}')                           #Outputs subtotal before tax
print(f'Sales Tax: ${((meal_cost+total_tip)*tax_rate):.2f}')                    #Outputs total sales tax
print(f'Total Cost: ${((meal_cost+total_tip)*tax_rate_multiplier):.2f}')        #Calculates and outputs total meal cost with tax
print()

time.sleep(1)                       #Fun time delay :)

print('I hope this helps! Go ahead and re-run this program if you would like to run the numbers again!')
print()




