heads = int(input("Total Heads: "))
legs = int(input("Total Legs: "))

# 4d + 2c = legs; d + c = heads
dogs = (legs - 2*heads)/2
chickens = heads - dogs

print(f"Dogs: {int(dogs)}, Chickens: {int(chickens)}")
