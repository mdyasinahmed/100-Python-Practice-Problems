# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

angle1 = int(input('Enter Value of Angle 1 : '))
angle2 = int(input('Enter Value of Angle 2 : '))
angle3 = int(input('Enter Value of Angle 3 : '))

sumOfAllAngles = angle1+angle2+angle3

print("Agnles are from one Triangle!") if sumOfAllAngles <= 180 else print("Agnles are not from one Triangle!")