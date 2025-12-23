# Write a program that will take three digits from the user and return the sum of the squares of each digit.
import numpy as np

digit1 = int(input('Enter Digit 1: '))
digit2 = int(input('Enter Digit 2: '))
digit3 = int(input('Enter Digit 3: '))


sum_Squares_Of_Three = np.sqrt(digit1) + np.sqrt(digit2) + np.sqrt(digit3)

print(sum_Squares_Of_Three)