# Write a program to find the simple interest when the value of the principal, rate of interest, and time period is given.

principalValue = float(input('Enter Value of Principal: '))
rateOFInterest = float(input('Enter Rate of Interest in %: '))
timePeriod = int(input('Enter a Time Period in Year(1/2/3): '))


simpleInterest = (principalValue*rateOFInterest*timePeriod)/100;

print(simpleInterest)