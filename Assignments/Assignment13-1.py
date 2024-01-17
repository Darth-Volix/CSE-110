'''
Week 13 Assignment: Wind Chill Calculations w/ Functions
Nicholas Wilkins 
12/08/2023
'''

# Define a function to calculate the wind chill based on a given temperature and wind speed
def wind_chill(temp, speed):
  return 35.74 + 0.6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)

# Define a function to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
  return celsius * (9/5) + 32

user_continue = 'yes'

while user_continue.lower() == 'yes':

    # Ask the user to enter the temperature in Celsius or Fahrenheit
    temp = input("\nEnter the temperature without adding a space at the end (ex. 13F or 15C): ")

    # Check if the temperature is in Celsius
    if temp[-1].upper() == "C":
        # Convert the temperature to Fahrenheit
        temp = celsius_to_fahrenheit(float(temp[:-1]))
        # Print the converted temperature
        print(f"The temperature in Fahrenheit is {temp:.2f}F")
    else:
        # Assume the temperature is in Fahrenheit
        temp = float(temp[:-1])

    # Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5
    for speed in range(5, 65, 5):
        # Calculate the wind chill for each wind speed
        chill = wind_chill(temp, speed)
        # Display the wind chill value to 2 decimals of precision
        print(f"At temperature {temp}F, the wind chill at {speed} mph is {chill:.2f}F")

    user_continue = input('\nWould you like to continue? (yes or no): ')

print('\nThank you! Goodbye.\n')