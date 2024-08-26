# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

number = int(input('Enter a Four Digit Number: '))

reversedNumber = int(str(number)[::-1])

if number==reversedNumber :
    print('Your Given Number is Palindrome!')
else :
    print('Your Given Number is Not Palindrome!')