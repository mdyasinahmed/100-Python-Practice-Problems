import math
num = int(input("Numerator: "))
den = int(input("Denominator: "))
common = math.gcd(num, den)
print(f"{num//common}/{den//common}")
