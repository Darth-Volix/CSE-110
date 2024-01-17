'''
Week 6 Team Activity: Amusement Park Rides
'''
# Rules:
## No one under 36 inches may ever ride, either by themselves or with another rider.
## Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
## If there are two riders and one of them is at least 18 years old, they may ride together.

# stretch challenge rules:
### If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
### If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
### If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

rider1_age = int(input('What is the age of the first rider?: '))
rider1_height = int(input('What is the height of the first rider? (in inches): '))
rider2 = input('Is there a second rider? (yes or no): ')
can_ride = None

if rider2.lower() == "yes": 
    rider2_age = int(input('What is the age of the second rider?: '))
    rider2_height = int(input('What is the height of the second rider? (in inches): '))
    # rule 1
    if rider2_height < 36 or rider1_height < 36:
        can_ride = False
    # stretch challenge age exceptions rules
    elif rider1_age < 18 and rider2_age < 18:
        if rider1_age >= 12 and rider2_age >= 12 and rider1_height >= 52 and rider2_height >= 52:
            can_ride = True
        elif rider1_age >= 16 and rider2_age >= 14 and rider1_height >= 36 and rider2_height >= 36:
            can_ride = True
        elif rider1_age >= 14 and rider2_age >= 16 and rider1_height >= 36 and rider2_height >= 36:
            can_ride = True
        # stretch challenge golden passport rule
        elif rider1_age < 18 and rider1_age >= 12:
            gldpass = input('Do you have a golden passport rider 1? (yes or no): ')
            if gldpass.lower() == 'yes' and rider1_height >= 36:
                can_ride = True
            elif gldpass.lower() != 'yes':
                if rider2_age < 18 and rider2_age >= 12:
                   gldpass = input('Do you have a golden passport rider 2? (yes or no): ')
                   if gldpass.lower() == 'yes' and rider2_height >= 36:  
                       can_ride = True 
                   else: 
                       can_ride = False
                else: 
                    can_ride = False
            else: 
                can_ride = False
        else:
            can_ride = False
    else:
        #rule 3
        if rider1_age >= 18 or rider2_age >= 18:
            can_ride = True
else:
    #rule 1 and 3
    if rider1_age >= 18 and rider1_height >= 62:
        can_ride = True
    #stretch challenge golden passport rule
    elif rider1_age < 18 and rider1_age >= 12:
        gldpass = input('Do you have a golden passport? (yes or no): ')
        if gldpass.lower() == 'yes' and rider1_height >= 62:
            can_ride = True
    else: 
        can_ride = False

if can_ride:
    print('You are allowed to ride!')
else:
    print('You are not allowed to ride.')
    