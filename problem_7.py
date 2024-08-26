# Write a program that will tell whether the given year is a leap year or not.

year = int(input('Enter a Year(EX: 2000) : '))

if year%4==0 and year%100!=0 :
    if year%400==0 :
        print(f"{year} is Leap Year.")
else:
    print(f"{year} is not Leap Year.")