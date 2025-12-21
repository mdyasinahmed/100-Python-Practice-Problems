a = int(input("Num 1: "))
b = int(input("Num 2: "))

res = 0

for _ in range(abs(b)): 
    res += a
    
print(res if b > 0 else -res)
