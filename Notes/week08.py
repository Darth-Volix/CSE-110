'''
Week 8: For loops
Sister Hansen
'''

# 1) loop to print 1 through 5 (using a range)
for x in range(1,6): # (1,2,3,4,5)
    print(x)
# loop to print odd values 1 though 11
print()
for x in range(1,12,2): # (1,3,5,7,9,11)
    print(x)

# 2) loop to print "Hello" a user specified number of times
print()
repeat = int(input('How many times should we print Hello?: ')) # all values that go into the range must be an integer
for x in range(repeat):
    print("Hello")

# 3) loop to print each letter in a string (two ways)
print()
my_string = "Hello"
for letter in my_string:
    print(letter)

print()
for i in range(len(my_string)): # i stands for index, len is for length (how many items in collection)
    print(my_string[i])

# 4) loop to print each item in a list
print()
my_list = [1,3,5,7,9]

for num in my_list:
    print(num)
    
print()
for i in range(len(my_list)):
    print(my_list[i])


# team activity - looping through strings 


# a variation on the stretch
first_name = "Brigham"
last_name = "Younger"

# use range and len to loop through the string
for i in range(len(first_name)):
    print(f"The letter {first_name[i]} is at position {i} in the first name")
    print(f"The letter {last_name[i]} is at position {i} in the last name")
    # we could also use if statements to check if the letters are the same