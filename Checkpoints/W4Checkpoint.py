import math

degrees_f = float(input('What is the temperature in Farenheight?: '))
degrees_c = (degrees_f - 32) * (5/9)

print(f'The temperature in Celcius is {degrees_c:.1f} degrees.')