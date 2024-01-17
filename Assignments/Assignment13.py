'''
Week 13 Assignment: Wind Chill Calculations w/ Functions
Nicholas Wilkins 
12/08/2023
'''
####### NEED TO COME BACK AND ADD SECOND FUNCTION #######
def wind_chill_calc(metric, temperature):
    starting_speed = 5
    while starting_speed < 65:
        if metric.lower() == 'f':
            windchill = 35.74 + 0.6215 * temperature - 35.75 * (starting_speed ** 0.16) + 0.4275 * temperature * (starting_speed ** 0.16)
            print(f'At temperature {temperature}F, and windspeed {starting_speed} mph, the windchill is: {windchill:.2f}F')
        elif metric.lower() == 'c':
            windchill = 13.12 + 0.6215 * temperature - 11.37 * (starting_speed ** 0.16) + 0.3965 * temperature * (starting_speed ** 0.16)
            print(f'At temperature {temperature}C, and windspeed {starting_speed} mph, the windchill is: {windchill:.2f}C')
        starting_speed = starting_speed + 5

print()
user_metric_choice = input('What temperature scale would you like to use? (type "F" or "C"): ')
user_temperature_choice = float(input('How cold is it outside?: '))
print()

wind_chill_calc(user_metric_choice, user_temperature_choice)