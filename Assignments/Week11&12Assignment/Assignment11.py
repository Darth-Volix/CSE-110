'''
Week 11 Assignment: Data Analysis - Life Expectancy 
Nicholas Wilkins
11/27/2023
'''
# Sets the variable to indicate the user would like to run the program
user_continue = 'yes'
print('\nWelcome To The World Database For Life Expectancy! (Through 2019)')

# Program will run as long as the user continues to indicate they would like to look through data
while user_continue.lower() == 'yes' or user_continue.lower() == 'sure' or user_continue.lower() == 'maybe':

    # Initialize the variables that will be used throughout the program 
    highest_expectancy = -999999
    lowest_expectancy = 999999
    user_highest_expectancy = -999999
    user_lowest_expectancy = 999999
    highest_expec_country = None
    lowest_expec_country = None
    highest_year = None
    lowest_year = None
    user_highest_country = None
    user_lowest_country = None
    user_average_life = 0
    counter = 0
    largest_drop = 0
    drop_country = None
    drop_year = None
    prev_life = None
    prev_country = None
    prev_year = None

    # User inputs the year they would like the information from 
    user_year = (input('\nWhat year would you like the life expectancy data for?: '))

    # Open the file with the Spanish Flu data
    with open('life-expectancy.csv') as file_var:
        # Skip the header from the file
        header = next(file_var)
        for line in file_var:
            # Strip whitespace from each line
            line = line.strip()
            # Split lines into parts, remembering that they are comma separated 
            line_list = line.split(',')
            
            # Turn line items into usable variables
            country = line_list[0]
            code = line_list[1]
            year = (line_list[2])
            life_expectancy = float(line_list[3])
            
            # If this is the first iteration, set the starting values for finding largest drop
            if prev_life == None and prev_country == None and prev_year == None:
                prev_life = life_expectancy
                prev_country = country
                prev_year = year
            else:
                # Check if the current country is the same as the previous one
                if country == prev_country:
                    # Check if the current year is one more than the previous one
                    if int(year) == int(prev_year) + 1:
                        # Calculate the difference between the current and previous life expectancy
                        diff = prev_life - life_expectancy
                        # Check if there is a drop in life expectancy
                        if diff > 0:
                            # Compare with the largest drop so far
                            if diff > largest_drop:
                                # Update the largest drop and the corresponding country and year
                                largest_drop = diff
                                drop_country = country
                                drop_year = year
                # Update the previous values
                prev_life = life_expectancy
                prev_country = country
                prev_year = year   
            # Find the highest life expectancy
            if life_expectancy > highest_expectancy:
                highest_expectancy = life_expectancy
                highest_expec_country = country
                highest_year = year
            # Find the lowest life expectancy 
            elif life_expectancy < lowest_expectancy:
                lowest_expectancy = life_expectancy
                lowest_expec_country = country
                lowest_year = year 
            # Program checks to see if the data matches the year the user indicated 
            elif user_year == year:
                # Calculate the average life expectancy (can't use sum because sum looks at an entire list while in this case
                # we are looking at one index of a list in multiple lists)
                user_average_life = user_average_life + life_expectancy
                counter = counter + 1
                average = user_average_life / counter
                # Find the highest and lowest life expectancy and their respective countries for the user indicated year
                if life_expectancy > user_highest_expectancy:
                    user_highest_expectancy = life_expectancy
                    user_highest_country = country
                elif life_expectancy < user_lowest_expectancy:
                    user_lowest_expectancy = life_expectancy
                    user_lowest_country = country   
        # Print the outputs of the highest and lowest life expectancy (the abs() function returns the absolute value as a way of printing a negative number as a positive number)
        print(f'\nThe overall max life expectancy is: {highest_expectancy} years from {highest_expec_country} in {highest_year}.')
        print(f'The overall min life expectancy is: {lowest_expectancy} years from {lowest_expec_country} in {lowest_year}.')
        print(f'The largest drop in life expectancy was {largest_drop:.2f} years in {drop_country} from {int(drop_year) - 1} to {drop_year}.')
        print(f'\nFor the year {user_year}:\nThe average life expectancy was {average:.2f} years.\nThe max life expectancy was in {user_highest_country}, which had a life expectancy of {user_highest_expectancy} years.\nThe min life expectancy was in {user_lowest_country}, which had a life expectancy of {user_lowest_expectancy} years.\n')
    # Program asks the user if they would like to continue
    user_continue = input('Would you like to see the data for another year? (type "yes" or "no"): ')
# User did not want to continue looking through data
print('\nThank you! Goodbye.\n')