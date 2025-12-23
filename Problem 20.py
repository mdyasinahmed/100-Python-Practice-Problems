salary = float(input("Enter Salary (Lakhs): "))

hra = 0.10 * salary
da = 0.05 * salary
pf = 0.03 * salary

# Tax calculation
if salary <= 1: 
    print("K")
elif salary <= 10: 
    tax = 0.10
elif salary <= 20: 
    tax = 0.20
else: 
    tax = 0.30
    
in_hand = salary - (hra + da + pf + (salary * tax))

print("In hand salary:", in_hand)
