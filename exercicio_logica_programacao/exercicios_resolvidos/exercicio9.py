import math

ray = float(input('whats the radius:  '))
height = float(input('what is the height: '))
volume = math.pi*(ray**2)*height
print(f"The volume of the oil can is {volume:.2f} cubic centimeters.")
