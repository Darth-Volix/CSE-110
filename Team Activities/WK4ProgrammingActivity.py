import math

print()
print('Welcome to the Velocity Calculator. Please enter the following:')
print()

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in ms^2, 9.8 for Earth or 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air or 1000 for water): '))
A = float(input('Cross Sectional Area (in m^2): '))
C = float(input('Drag Constant (0.5 for sphere or 1.1 for cylinder): '))
print()

c = (1/2) * p * A * C
V = (math.sqrt((m*g)/c)) * (1-math.exp((-math.sqrt(m*g*c)/m)*t))

print(f'The inner value of c is: {c:.3f}')
print(f'The Velocity after {t} seconds is: {V:.3f} m/s.')
print()