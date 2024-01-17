'''
Week 3: Variables and Expressions(math)
Sister Hansen
'''

#### Which are each of the following? (string, int, float)
x = '10'    #string
y = 5       #integer
z = 3.14    #float
print(x*5, y, z*2)

#### What do the following do?
x = int(x)     #int is a function that converts the variable to an integer
y = float(y)   #float is a function that converts the variable to a float (it is safer to use float in case the user inputs a decimal)
z = str(z)     #str is a function that converts the variable to a string

print(x, y, z+2)    #z+2 will fail because z is a string in this code. You also can't multiply a string by a float. 

#### Which is better? (they accomplish the same thing)
print("I have " + str(x) + " cats.")
print(f"I have {x} cats.")                 #I prefer the f string because of how easy it is

#### Order of operations
#### math operations and order of operations
'''
Operator	Description
()	        Parentheses
**	        Exponent
* / // %	Multiply, Divide, Floor divide, Modulo    (floor divide gives you a whole number without the remainer, modulo gives you the remainder)
+ -	        Addition, Subtraction
= 	        Assign
'''

#### What is stored in a, b, c and d? 
a = 10 + (4 * 2) - 3  # 15
b = 5 % 2             # 1
c = 5 // 2            # 2
d = 5 / 2             # 2.5
e = 2 / 2
print(f'math {a}, modulo {b}, floor divide {c}, normal divide {d}, divide ints {e}')

#### Team Activity
## Core requirements: 
# get user input (be able to handle ints or floats)
# convert it to a number so you can do some math with it (float)
# calculate areas of 3 shapes

# side = ???(input('What\'s the length of one side: '))
