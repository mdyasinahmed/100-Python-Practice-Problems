# Write a program to find the volume of a cylinder. Also, find the cost when the cost of 1 litre of milk is 40 Rs.
import math

radius = float(input('Enter Radius of Cylinder: '))
height = float(input('Enter Height of Cylinder: '))

volumeOFCylinder = math.pi*math.pow(radius, 2)*height

volumeINLiters = volumeOFCylinder/1000

costOFMilk = volumeINLiters*40

print(f"Volume Of Cylinder: {volumeOFCylinder}")
print(f"Cost of Milk: {costOFMilk}")