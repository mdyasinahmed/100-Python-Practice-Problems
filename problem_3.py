# User will input (2numbers).Write a program to swap the numbers

number1 = int(input('Number 1 : '))
number2 = int(input('Number 2 : '))

temp = number2
number2 = number1
number1 = temp

print(f"Number 1: {number1} 'and Number 2: ' {number2}")