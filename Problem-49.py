nums = []
while True:
    n = int(input("Enter number: "))
    if n == 0: break
    nums.append(n)
print(f"Sum: {sum(nums)}, Avg: {sum(nums)/len(nums)}")
