#Here is a program to check whether a number is a palindrome or not.

# Reverse a four-digit number and check whether it is a palindrome.

number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    print("Reversed number:", reversed_number)

    if original == reversed_number:
        print("Your given number is a palindrome!")
    else:
        print("Your given number is not a palindrome!")
else:
    print("Please enter a valid four-digit number.")
