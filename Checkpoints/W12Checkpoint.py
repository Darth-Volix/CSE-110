'''
Week 12 Checkpoint: Iterating Through List of People
Nicholas Wilkins
11/28/2023
'''
# List of people and their ages
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Setting the variables for youngest age and name
youngest_age = 999999
youngest_name = None

# Break the list into parts
for person in people:
    # Remove whitespace
    remove = person.strip()
    # Split the lines into parts
    pieces = remove.split()

    # Set the variables for the line pieces
    name = pieces[0]
    age = int(pieces[1])

    # Search for the youngest age and the corresponding name
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

# Output the results
print(f'\nThe person with the youngest age is {youngest_name}, who is {youngest_age} years old.\n')



