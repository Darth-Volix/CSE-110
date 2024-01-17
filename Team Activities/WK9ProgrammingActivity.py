'''
Week 9 Team Activity: Lists of Numbers
Nicholas Wilkins
11/06/2023
'''
user_num = None
numbers = []

while user_num != 0:
    user_num = int(input('Please enter a whole number: '))
    if user_num != 0:
        numbers.append(user_num)

total_of_numbers = 0
for number in numbers:
    total_of_numbers += number

# The above function could be written as the following:
# total_of_numbers = sum(numbers)

print(f'The sum of the numbers is {total_of_numbers}')
print(f'The average of the numbers is {total_of_numbers / len(numbers)}')
print(f'The largest number is {max(numbers)}')    # prints the largest number in the list

smallest_number = 999999999
for number in numbers:
    if number > 0 and number < smallest_number:
        smallest_number = number

print(f'The smallest positive number is {smallest_number}')

sorted_numbers = sorted(numbers)
print(f'The sorted list is: {sorted_numbers}')

