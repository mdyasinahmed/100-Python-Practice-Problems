num = int(input("Number: "))

s_num = str(num)
power = len(s_num)

res = sum(int(digit)**power for digit in s_num)

print("Yes" if res == num else "No")
